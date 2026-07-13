app.route("/materias-primas", methods=["GET"])
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