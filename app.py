from flask import Flask, request, jsonify
import numpy as np
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "service": "flask"}

@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json.get("values", [])

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    data = [float(x) for x in data]

    avg = float(np.mean(data))
    trend = float((data[-1] - data[0]) / len(data))
    future = float(data[-1] + trend)

    return jsonify({
        "promedio": avg,
        "tendencia": trend,
        "proyeccion": future
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
