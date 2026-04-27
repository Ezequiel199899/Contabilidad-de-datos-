   
 mkdir backend-flask
mkdir backend-spring.  from flask import Flask, request, jsonify
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
    app.run(host="0.0.0.0", port=port).    flask
numpy.      FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"].     git init
git add .
git commit -m "init: microservicio flask con forecast"    server.port=${PORT:8080}.   import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class AccountingController {

    private final RestTemplate restTemplate = new RestTemplate();

    @GetMapping("/")
    public Map<String, String> home() {
        return Map.of("status", "ok");
    }

    @PostMapping("/analyze")
    public Map<String, Object> analyze(@RequestBody List<Map<String, Object>> data) {

        List<Double> amounts = data.stream()
                .map(row -> Double.parseDouble(row.get("amount").toString()))
                .toList();

        Map<String, Object> body = Map.of("values", amounts);

        Object forecast = restTemplate.postForObject(
                "https://flask-abc123.onrender.com/forecast",
                body,
                Object.class
        );

        return Map.of("forecast", forecast);
    }
}.   FROM eclipse-temurin:17

WORKDIR /app

COPY target/app.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"].   git add .
git commit -m "feat: API spring conectada a flask". git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git push -u origin main.  git add .
git commit -m "feat: integración con flask en render"
git push.  backend-flask/
backend-spring/ init: microservicio flask con forecast
feat: API spring conectada a flask
feat: integración con flask en render   