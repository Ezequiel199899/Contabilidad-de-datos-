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
    app.run(host="0.0.0.0", port=port).     flask
numpy.      FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"].   server.port=${PORT:8080}.    @RestController
@RequestMapping("/api")
public class AccountingController {

    private final RestTemplate restTemplate = new RestTemplate();

    @GetMapping("/")
    public Map<String, String> home() {
        return Map.of(
                "status", "ok",
                "service", "financial API",
                "endpoints", "/api/analyze, /api/rates, /api/commodities"
        );
    }

    @PostMapping("/analyze")
    public Map<String, Object> analyze(@RequestBody List<Map<String, Object>> data) {

        List<Double> amounts = data.stream()
                .map(row -> Double.parseDouble(row.get("amount").toString()))
                .toList();

        Map<String, Object> body = Map.of("values", amounts);

        Object forecast = restTemplate.postForObject(
                "https://TU-FLASK-URL.onrender.com/forecast",
                body,
                Object.class
        );

        return Map.of(
                "datos", data,
                "forecast", forecast
        );
    }

    @GetMapping("/rates")
    public Map<String, Double> getRates() {
        return Map.of(
                "USD", 1.0,
                "EUR", 1.17,
                "ARS", 900.0,
                "BRL", 5.0
        );
    }

    @GetMapping("/commodities")
    public Map<String, Double> getCommodities() {
        return Map.of(
                "gold", 5000.0,
                "silver", 84.0,
                "oil", 80.0,
                "soy", 450.0
        );
    }
}.       "https://flask-xxxx.onrender.com/forecast"            