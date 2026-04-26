 version: "3.9"

services:

  flask:
    build: ./backend-flask
    container_name: flask-service
    ports:
      - "5000:5000"

  spring:
    build: ./backend-spring
    container_name: spring-service
    ports:
      - "8080:8080"
    depends_on:
      - flask.     from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

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
    app.run(host="0.0.0.0", port=5000).    flask
numpy.      FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"].    FROM eclipse-temurin:17

WORKDIR /app

COPY target/app.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"].    docker-compose up --build.   