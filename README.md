 from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/forecast", methods=["POST"])
def forecast():
    try:
        data = request.json.get("values", [])

        if not data or not isinstance(data, list):
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
    app.run(port=5000, debug=True)    @RestController
@RequestMapping("/api")
public class AccountingController {

    private final RestTemplate restTemplate = new RestTemplate();

    @PostMapping("/analyze")
    public Map<String, Object> analyze(@RequestBody List<Map<String, Object>> data) {

        List<Double> amounts = data.stream()
                .map(row -> Double.parseDouble(row.get("amount").toString()))
                .toList();

        Map<String, Object> body = Map.of("values", amounts);

        Object forecast = restTemplate.postForObject(
                "http://localhost:5000/forecast",
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
                "GBP", 1.35,
                "BRL", 0.20
        );
    }

    @GetMapping("/commodities")
    public Map<String, Double> getCommodities() {
        return Map.of(
                "gold", 5000.0,
                "silver", 84.0,
                "oil", 80.0
        );
    }
}.         async function analizarDatos(data) {
  try {
    const res = await fetch("http://localhost:8080/api/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!res.ok) throw new Error("API error");

    const result = await res.json();
    console.log("Resultado:", result);

  } catch (error) {
    console.error("Error:", error);
  }
}

analizarDatos([
  { amount: 100 },
  { amount: 50 },
  { amount: 200 }
]);          flask
numpy.      