
>
       from flask import Flask, request, jsonify
import numpy as np
import os
import requests
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ---------- "Bases de datos" en memoria (reemplazar por PostgreSQL en producción) ----------
TRANSACCIONES = {}   # id -> {"monto": float, "descripcion": str}
HISTORIAL_IA = {}    # clave -> [ {"pregunta":..., "respuesta":...}, ... ]

# API key opcional para un proveedor de materias primas (ej: metals-api.com, commodities-api.com)
MATERIAS_PRIMAS_API_KEY = os.environ.get("MATERIAS_PRIMAS_API_KEY")


# ======================================================================
# Utilidades generales
# ======================================================================
def calcular_metricas(valores):
    valores = [float(x) for x in valores]
    avg = float(np.mean(valores))
    tendencia = float((valores[-1] - valores[0]) / len(valores))
    proyeccion = float(valores[-1] + tendencia)
    return avg, tendencia, proyeccion


def preguntar_ia(contexto, pregunta, rol="analista financiero"):
    prompt = f"""Sos un {rol}. Respondé en español, claro y breve,
como lo haría un profesional explicándole a un dueño de PyME.

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


def guardar_historial(clave, pregunta, respuesta):
    HISTORIAL_IA.setdefault(clave, []).append({"pregunta": pregunta, "respuesta": respuesta})


@app.route("/")
def home():
    return {"status": "ok", "service": "flask"}


# ======================================================================
# Forecasting financiero (original)
# ======================================================================
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
        return jsonify({"error": "Faltan 'id' o 'monto'"}), 400

    TRANSACCIONES[tid] = {"monto": float(monto), "descripcion": descripcion}
    return jsonify({"status": "creada", "id": tid}), 201


# ======================================================================
# IA sobre datos financieros / contables
# ======================================================================
@app.route("/ai/consultar", methods=["POST"])
def consultar_ia():
    body = request.json
    pregunta = body.get("pregunta")
    datos = body.get("datos", [])

    if not pregunta or not datos:
        return jsonify({"error": "Faltan 'pregunta' o 'datos'"}), 400

    avg, tendencia, proyeccion = calcular_metricas(datos)
    contexto = f"Valores: {datos}\nPromedio: {avg:.2f} | Tendencia: {tendencia:.2f} | Proyección: {proyeccion:.2f}"
    respuesta = preguntar_ia(contexto, pregunta)
    guardar_historial("general", pregunta, respuesta)

    return jsonify({
        "respuesta": respuesta,
        "metricas": {"promedio": avg, "tendencia": tendencia, "proyeccion": proyeccion}
    })


@app.route("/ai/consultar/<tid>", methods=["POST"])
def consultar_transaccion(tid):
    pregunta = request.json.get("pregunta")
    transaccion = TRANSACCIONES.get(tid)

    if not transaccion:
        return jsonify({"error": f"No existe la transacción {tid}"}), 404
    if not pregunta:
        return jsonify({"error": "Falta 'pregunta'"}), 400

    contexto = f"Transacción {tid}: monto={transaccion['monto']}, descripción='{transaccion['descripcion']}'"
    respuesta = preguntar_ia(contexto, pregunta)
    guardar_historial(tid, pregunta, respuesta)

    return jsonify({"id": tid, "respuesta": respuesta})


@app.route("/ai/anomalias", methods=["POST"])
def detectar_anomalias():
    datos = request.json.get("datos", [])
    if not datos:
        return jsonify({"error": "Faltan 'datos'"}), 400

    valores = np.array([float(x) for x in datos])
    desvio = valores.std() if valores.std() > 0 else 1e-9
    z_scores = (valores - valores.mean()) / desvio

    anomalias = [
        {"indice": i, "valor": float(v), "z_score": float(z)}
        for i, (v, z) in enumerate(zip(valores, z_scores)) if abs(z) > 2
    ]

    if not anomalias:
        return jsonify({"anomalias": [], "explicacion": "No se detectaron variaciones anómalas."})

    contexto = f"Datos: {datos}\nAnomalías (z-score > 2): {anomalias}"
    explicacion = preguntar_ia(contexto, "Explicá brevemente por qué estos valores son anómalos y qué revisar.")
    return jsonify({"anomalias": anomalias, "explicacion": explicacion})


# ======================================================================
# Divisas / tipos de cambio
# ======================================================================
def obtener_tipo_cambio(base, destino):
    """Usa Frankfurter (API pública, gratuita, sin key) para tipos de cambio de referencia."""
    url = f"https://api.frankfurter.app/latest?from={base}&to={destino}"
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
            return jsonify({"error": f"No se encontró cotización {base}->{destino}"}), 404
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
        return jsonify({"error": "Falta 'pregunta'"}), 400

    try:
        tasa = obtener_tipo_cambio(base, destino)
    except requests.RequestException as e:
        return jsonify({"error": "No se pudo obtener el tipo de cambio", "detalle": str(e)}), 502

    contexto = f"Tipo de cambio actual {base}->{destino}: {tasa}"
    respuesta = preguntar_ia(contexto, pregunta, rol="analista de mercado de divisas")
    guardar_historial(f"divisas:{base}{destino}", pregunta, respuesta)

    return jsonify({"base": base, "destino": destino, "tasa": tasa, "respuesta": respuesta})


# ======================================================================
# Materias primas (commodities)
# ======================================================================
def obtener_precio_materia_prima(nombre):
    """
    Stub listo para conectar a un proveedor real (metals-api.com, commodities-api.com, etc).
    Si hay MATERIAS_PRIMAS_API_KEY configurada, se puede reemplazar esta función por
    la llamada real a ese proveedor. Por ahora devuelve None si no hay key.
    """
    if not MATERIAS_PRIMAS_API_KEY:
        return None
    # Ejemplo de integración real (ajustar a la API que elijas):
    # r = requests.get(
    #     f"https://api.metals-api.com/v1/latest?access_key={MATERIAS_PRIMAS_API_KEY}&symbols={nombre}"
    # )
    # return r.json()["rates"][nombre]
    return None


@app.route("/materias-primas", methods=["GET"])
def ver_materia_prima():
    nombre = request.args.get("nombre", "").upper()
    if not nombre:
        return jsonify({"error": "Falta el parámetro 'nombre' (ej: XAU para oro, WTI para petróleo)"}), 400

    precio = obtener_precio_materia_prima(nombre)
    if precio is None:
        return jsonify({
            "error": "Sin proveedor de materias primas configurado",
            "detalle": "Seteá MATERIAS_PRIMAS_API_KEY y conectá tu proveedor en obtener_precio_materia_prima()"
        }), 501

    return jsonify({"nombre": nombre, "precio": precio})


@app.route("/ai/consultar-materias-primas", methods=["POST"])
def consultar_materias_primas():
    body = request.json
    pregunta = body.get("pregunta")
    nombre = body.get("nombre", "").upper()
    datos = body.get("datos")  # opcional: serie histórica que ya tenga el usuario

    if not pregunta:
        return jsonify({"error": "Falta 'pregunta'"}), 400

    if datos:
        avg, tendencia, proyeccion = calcular_metricas(datos)
        contexto = (
            f"Materia prima: {nombre or 'no especificada'}\n"
            f"Serie de precios: {datos}\n"
            f"Promedio: {avg:.2f} | Tendencia: {tendencia:.2f} | Proyección: {proyeccion:.2f}"
        )
    else:
        precio = obtener_precio_materia_prima(nombre) if nombre else None
        if precio is None:
            return jsonify({
                "error": "No hay precio disponible",
                "detalle": "Pasá 'datos' con una serie histórica, o configurá MATERIAS_PRIMAS_API_KEY"
            }), 400
        contexto = f"Materia prima: {nombre}\nPrecio actual: {precio}"

    respuesta = preguntar_ia(contexto, pregunta, rol="analista de materias primas y commodities")
    guardar_historial(f"materias_primas:{nombre or 'general'}", pregunta, respuesta)

    return jsonify({"nombre": nombre, "respuesta": respuesta})


# ======================================================================
# Historial de consultas
# ======================================================================
@app.route("/ai/historial/<clave>", methods=["GET"])
def ver_historial(clave):
    return jsonify(HISTORIAL_IA.get(clave, []))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
