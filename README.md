 from flask import Flask, request, jsonify
import numpy as np
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "service": "flask forecast API"}

@app.route("/forecast", methods=["POST"])
def forecast():
    try:
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

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port).    flask
numpy.      FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"].     server.port=${PORT:8080}.      FROM eclipse-temurin:17

WORKDIR /app

COPY target/app.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"].    