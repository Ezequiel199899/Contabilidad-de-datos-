from flask import Flask, request, jsonify
import numpy as np
import os
import requests
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

TRANSACCIONES = {}
HISTORIAL_IA = {}
MATERIAS_PRIMAS_API_KEY = os.environ.get("MATERIAS_PRIMAS_API_KEY")


def calcular_metricas(valores):
    valores = [float(x) for x in valores]
    avg = float(np.mean(valores))
    tendencia = float((valores[-1] - valores[0]) / len(valores))
    proyeccion = float(valores[-1] + tendencia)
    return avg, tendencia, proyeccion


def preguntar_ia(contexto, pregunta, rol="analista financiero"):
    prompt = "Sos un " + rol + ". Respondé en español, claro y breve, como lo haria un profesional explicandole a un dueno de PyME.\n\nContexto de datos:\n" + contexto + "\n\nPregunta del usuario: " + pregunta
    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return respuesta.content[0].text


def guardar_historial(clave, pregunta, respuesta):
    HISTORIAL_IA.setdefault(clave, []).append({"pregunta": pregunta, "respuesta": respuesta})


@app.route("/")
def home():
    return {"status": "ok", "service": "flask"}


@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json.get("values", [])
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    avg, tendencia, proyeccion = calcular_metricas(data)
    return jsonify({"promedio": avg, "tendencia": tendencia, "proyeccion": proyeccion})


@app.route("/transacciones", methods=["POST"])
def crear_transaccion():
    body = request.json
    tid = str(body.get("id"))
    monto = body.get("monto")
    descripcion = body.get("descripcion", "")
    if not tid or monto is None:
        return jsonify({"error": "Faltan id o monto"}), 400
    TRANSACCIONES[tid] = {"monto": float(monto), "descripcion": descripcion}
    return jsonify({"status": "creada", "id": tid}), 201


@app.route("/ai/consultar", methods=["POST"])
def consultar_ia():
    body = request.json
    pregunta = body.get("pregunta")
    datos = body.get("datos", [])
    if not pregunta or not datos:
        return jsonify({"error": "Faltan pregunta o datos"}), 400
    avg, tendencia, proyeccion = calcular_metricas(datos)
    contexto = "Valores: " + str(datos) + "\nPromedio: " + str(round(avg,2)) + " | Tendencia: " + str(round(tendencia,2)) + " | Proyeccion: " + str(round(proyeccion,2))
    respuesta = preguntar_ia(contexto, pregunta)
    guardar_historial("general", pregunta, respuesta)
    return jsonify({"respuesta": respuesta, "metricas": {"promedio": avg, "tendencia": tendencia, "proyeccion": proyeccion}})


@app.route("/ai/consultar/<tid>", methods=["POST"])
def consultar_transaccion(tid):
    pregunta = request.json.get("pregunta")
    transaccion = TRANSACCIONES.get(tid)
    if not transaccion:
        return jsonify({"error": "No existe la transaccion " + tid}), 404
    if not pregunta:
        return jsonify({"error": "Falta pregunta"}), 400
    contexto = "Transaccion " + tid + ": monto=" + str(transaccion["monto"]) + ", descripcion=" + transaccion["descripcion"]
    respuesta = preguntar_ia(contexto, pregunta)
    guardar_historial(tid, pregunta, respuesta)
    return jsonify({"id": tid, "respuesta": respuesta})


@app.route("/ai/anomalias", methods=["POST"])
def detectar_anomalias():
    datos = request.json.get("datos", [])
    if not datos:
        return jsonify({"error": "Faltan datos"}), 400
    valores = np.array([float(x) for x in datos])
    desvio = valores.std() if valores.std() > 0 else 1e-9
    z_scores = (valores - valores.mean()) / desvio
    anomalias = []
    for i in range(len(valores)):
        if abs(z_scores[i]) > 2:
            anomalias.append({"indice": i, "valor": float(valores[i]), "z_score": float(z_scores[i])})
    if not anomalias:
        return jsonify({"anomalias": [], "explicacion": "No se detectaron variaciones anomalas."})
    contexto = "Datos: " + str(datos) + "\nAnomalias (z-score > 2): " + str(anomalias)
    explicacion = preguntar_ia(contexto, "Explica brevemente por que estos valores son anomalos y que revisar.")
    return jsonify({"anomalias": anomalias, "explicacion": explicacion})


def obtener_tipo_cambio(base, destino):
    url = "https://api.frankfurter.app/latest?from=" + base + "&to=" + destino
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["rates"].get(destino)


@app.route("/divisas", methods=["GET"])
def ver_divisa():
    base = request.args.get("base", "USD").upper()
    destino = request.args.get("destino", "EUR").upper()
    try:
        tasa = obtener_tipo_cambio(base, destino)
        if tasa is None:
            return jsonify({"error": "No se encontro cotizacion " + base + "->" + destino}), 404
        return jsonify({"base": base, "destino": destino, "tasa": tasa})
    except requests.RequestException as e:
        return jsonify({"error": "No se pudo obtener el tipo de cambio", "detalle": str(e)}), 502


@app.route("/ai/consultar-divisas", methods=["POST"])
def consultar_divisas():
    body = request.json
    pregunta = body.get("pregunta")
    base = body.get("base", "USD").upper()
    destino = body.get("destino", "EUR").upper()
    if not pregunta:
        return jsonify({"error": "Falta pregunta"}), 400
    try:
        tasa = obtener_tipo_cambio(base, destino)
    except requests.RequestException as e:
        return jsonify({"error": "No se pudo obtener el tipo de cambio", "detalle": str(e)}), 502
    contexto = "Tipo de cambio actual " + base + "->" + destino + ": " + str(tasa)
    respuesta = preguntar_ia(contexto, pregunta, rol="analista de mercado de divisas")
    guardar_historial("divisas:" + base + destino, pregunta, respuesta)
    return jsonify({"base": base, "destino": destino, "tasa": tasa, "respuesta": respuesta})


def obtener_precio_materia_prima(nombre):
    if not MATERIAS_PRIMAS_API_KEY:
        return None
    return None


@app.route("/materias-primas", methods=["GET"])
def ver_materia_prima():
    nombre = request.args.get("nombre", "").upper()
    if not nombre:
        return jsonify({"error": "Falta el parametro nombre (ej: XAU para oro, WTI para petroleo)"}), 400
    precio = obtener_precio_materia_prima(nombre)
    if precio is None:
        return jsonify({"error": "Sin proveedor de materias primas configurado", "detalle": "Setea MATERIAS_PRIMAS_API_KEY"}), 501
    return jsonify({"nombre": nombre, "precio": precio})


@app.route("/ai/consultar-materias-primas", methods=["POST"])
def consultar_materias_primas():
    body = request.json
    pregunta = body.get("pregunta")
    nombre = body.get("nombre", "").upper()
    datos = body.get("datos")
    if not pregunta:
        return jsonify({"error": "Falta pregunta"}), 400
    if datos:
        avg, tendencia, proyeccion = calcular_metricas(datos)
        contexto = "Materia prima: " + (nombre or "no especificada") + "\nSerie de precios: " + str(datos) + "\nPromedio: " + str(round(avg,2)) + " | Tendencia: " + str(round(tendencia,2)) + " | Proyeccion: " + str(round(proyeccion,2))
    else:
        precio = obtener_precio_materia_prima(nombre) if nombre else None
        if precio is None:
            return jsonify({"error": "No hay precio disponible", "detalle": "Pasa datos con una serie historica, o configura MATERIAS_PRIMAS_API_KEY"}), 400
        contexto = "Materia prima: " + nombre + "\nPrecio actual: " + str(precio)
    respuesta = preguntar_ia(contexto, pregunta, rol="analista de materias primas y commodities")
    guardar_historial("materias_primas:" + (nombre or "general"), pregunta, respuesta)
    return jsonify({"nombre": nombre, "respuesta": respuesta})


@app.route("/ai/historial/<clave>", methods=["GET"])
def ver_historial(clave):
    return jsonify(HISTORIAL_IA.get(clave, []))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
 