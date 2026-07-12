from flask import Flask, request, jsonify
import numpy as np
import os
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Memoria simple en proceso para guardar transacciones y su historial de consultas.
# En producción esto debería vivir en PostgreSQL (ya lo tenés en el stack).
TRANSACCIONES = {}   # id -> {"monto": float, "descripcion": str}
HISTORIAL_IA = {}    # id o "general" -> [ {"pregunta":..., "respuesta":...}, ... ]


def calcular_metricas(valores):
    valores = [float(x) for x in valores]
    avg = float(np.mean(valores))
    tendencia = float((valores[-1] - valores[0]) / len(valores))
    proyeccion = float(valores[-1] + tendencia)
    return avg, tendencia, proyeccion


def preguntar_ia(contexto, pregunta):
    prompt = f"""Sos un asistente financiero contable. Respondé en español, claro y breve,
como lo haría un analista senior explicándole a un dueño de PyME.

Contexto de datos:
{contexto}

Pregunta del usuario: {pregunta}
"""
    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.content[0].text


@app.route("/")
def home():
    return {"status": "ok", "service": "flask"}


# ---------- Forecasting original ----------
@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json.get("values", [])
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    avg, tendencia, proyeccion = calcular_metricas(data)
    return jsonify({
        "promedio": avg,
        "tendencia": tendencia,
        "proyeccion": proyeccion
    })


# ---------- Registrar transacciones (para poder consultarlas después por id) ----------
@app.route("/transacciones", methods=["POST"])
def crear_transaccion():
    body = request.json
    tid = str(body.get("id"))
    monto = body.get("monto")
    descripcion = body.get("descripcion", "")

    if not tid or monto is None:
        return jsonify({"error": "Faltan 'id' o 'monto'"}), 400

    TRANSACCIONES[tid] = {"monto": float(monto), "descripcion": descripcion}
    return jsonify({"status": "creada", "id": tid}), 201


# ---------- Consulta general en lenguaje natural sobre un conjunto de datos ----------
@app.route("/ai/consultar", methods=["POST"])
def consultar_ia():
    body = request.json
    pregunta = body.get("pregunta")
    datos = body.get("datos", [])

    if not pregunta or not datos:
        return jsonify({"error": "Faltan 'pregunta' o 'datos'"}), 400

    avg, tendencia, proyeccion = calcular_metricas(datos)
    contexto = f"Valores: {datos}\nPromedio: {avg:.2f} | Tendencia: {tendencia:.2f} | Proyección: {proyeccion:.2f}"

    texto_respuesta = preguntar_ia(contexto, pregunta)

    HISTORIAL_IA.setdefault("general", []).append(
        {"pregunta": pregunta, "respuesta": texto_respuesta}
    )

    return jsonify({
        "respuesta": texto_respuesta,
        "metricas": {"promedio": avg, "tendencia": tendencia, "proyeccion": proyeccion}
    })


# ---------- Consulta puntual sobre UNA transacción/acción específica ----------
@app.route("/ai/consultar/<tid>", methods=["POST"])
def consultar_transaccion(tid):
    pregunta = request.json.get("pregunta")
    transaccion = TRANSACCIONES.get(tid)

    if not transaccion:
        return jsonify({"error": f"No existe la transacción {tid}"}), 404
    if not pregunta:
        return jsonify({"error": "Falta 'pregunta'"}), 400

    contexto = f"Transacción {tid}: monto={transaccion['monto']}, descripción='{transaccion['descripcion']}'"
    texto_respuesta = preguntar_ia(contexto, pregunta)

    HISTORIAL_IA.setdefault(tid, []).append(
        {"pregunta": pregunta, "respuesta": texto_respuesta}
    )

    return jsonify({"id": tid, "respuesta": texto_respuesta})


# ---------- Detección simple de anomalías con explicación de la IA ----------
@app.route("/ai/anomalias", methods=["POST"])
def detectar_anomalias():
    datos = request.json.get("datos", [])
    if not datos:
        return jsonify({"error": "Faltan 'datos'"}), 400

    valores = np.array([float(x) for x in datos])
    media = valores.mean()
    desvio = valores.std() if valores.std() > 0 else 1e-9
    z_scores = (valores - media) / desvio

    anomalias = [
        {"indice": i, "valor": float(v), "z_score": float(z)}
        for i, (v, z) in enumerate(zip(valores, z_scores))
        if abs(z) > 2
    ]

    if not anomalias:
        return jsonify({"anomalias": [], "explicacion": "No se detectaron variaciones anómalas."})

    contexto = f"Datos: {datos}\nAnomalías detectadas (z-score > 2): {anomalias}"
    explicacion = preguntar_ia(contexto, "Explicá brevemente por qué estos valores son anómalos y qué revisar.")

    return jsonify({"anomalias": anomalias, "explicacion": explicacion})


# ---------- Historial de consultas ----------
@app.route("/ai/historial/<clave>", methods=["GET"])
def ver_historial(clave):
    return jsonify(HISTORIAL_IA.get(clave, []))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
 bpackage com.contabilidad.api.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api/ai")
public class AiController {

    @Value("${flask.base-url:http://localhost:5000}")
    private String flaskBaseUrl;

    private final RestTemplate restTemplate = new RestTemplate();

    // POST /api/ai/consultar  -> reenvía a Flask /ai/consultar
    @PostMapping("/consultar")
    public ResponseEntity<Map> consultar(@RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/consultar";
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // POST /api/ai/consultar/{id} -> reenvía a Flask /ai/consultar/{id}
    @PostMapping("/consultar/{id}")
    public ResponseEntity<Map> consultarTransaccion(
            @PathVariable String id,
            @RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/consultar/" + id;
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // POST /api/ai/anomalias -> reenvía a Flask /ai/anomalias
    @PostMapping("/anomalias")
    public ResponseEntity<Map> anomalias(@RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/anomalias";
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // GET /api/ai/historial/{clave} -> reenvía a Flask /ai/historial/{clave}
    @GetMapping("/historial/{clave}")
    public ResponseEntity<Object[]> historial(@PathVariable String clave) {
        String url = flaskBaseUrl + "/ai/historial/" + clave;
        Object[] respuesta = restTemplate.getForObject(url, Object[].class);
        return ResponseEntity.ok(respuesta);
    }
}

   