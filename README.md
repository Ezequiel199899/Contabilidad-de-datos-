 from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json["values"]

    avg = np.mean(data)
    trend = (data[-1] - data[0]) / len(data)
    future = data[-1] + trend

    return jsonify({
        "promedio": float(avg),
        "tendencia": float(trend),
        "proyeccion": float(future)
    })

if __name__ == "__main__":
    app.run(port=5000).         pip install flask numpy
python model.py.   package com.example.demo;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.*;

@RestController
@RequestMapping("/api")
public class AccountingController {

    @PostMapping("/analyze")
    public Map<String, Object> analyze(@RequestBody List<Map<String, Object>> data) {

        List<Double> amounts = new ArrayList<>();

        for (Map<String, Object> row : data) {
            amounts.add(Double.parseDouble(row.get("amount").toString()));
        }

        RestTemplate restTemplate = new RestTemplate();

        Map<String, Object> body = new HashMap<>();
        body.put("values", amounts);

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
}.      async function analizarDatos(data) {
  const res = await fetch("http://localhost:8080/api/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await res.json();

  console.log("Resultado completo:", result);
  console.log("Forecast:", result.forecast);
}.    const data = [
  { amount: 100, type: "ingreso" },
  { amount: 50, type: "egreso" },
  { amount: 200, type: "ingreso" }
];

analizarDatos(data);         # Python
http://localhost:5000

# Java (Spring Boot)
http://localhost:8080.      {
  "datos": [...],
  "forecast": {
    "promedio": 116.6,
    "tendencia": 33.3,
    "proyeccion": 233.3
  }
}.      