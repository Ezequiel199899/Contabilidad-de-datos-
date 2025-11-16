  
<!DOCTYPE html>
<html>
<head>
    <title>Finanzas AI – Sistema Contable Multimoneda</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h1>Finanzas AI</h1>
<h3>Asientos contables automáticos bimonetarios con IA</h3>

<p>Precio de lanzamiento: <b>$19.990 ARS</b></p>

<h2>Compra con PayPal</h2>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_blank">
    <input type="hidden" name="cmd" value="_xclick">
    <input type="hidden" name="business" value="TU_CORREO_PAYPAL@MAIL.COM">
    <input type="hidden" name="item_name" value="Finanzas AI – App">
    <input type="hidden" name="amount" value="19990">
    <input type="hidden" name="currency_code" value="ARS">
    <button type="submit">Comprar con PayPal</button>
</form>

<h2>MercadoPago</h2>
<a href="ENLACE_MERCADOPAGO" target="_blank">
    <button>Pagar con MercadoPago</button>
</a>

<h2>Tarjetas Visa / Mastercard / Naranja / AMEX</h2>
<a href="ENLACE_PROCESADOR_TARJETAS" target="_blank">
    <button>Pagar con Tarjeta</button>
</a>

<script src="app.js"></script>
</body>
</html>body {
    font-family: Arial;
    padding: 40px;
    background: #f1f1f1;
}

button {
    padding: 12px;
    border-radius: 8px;
    border: none;
    background: #0070f3;
    color: white;
    margin-top: 10px;
    cursor: pointer;
}

button:hover {
    opacity: 0.8;
}console.log("Finanzas AI app cargada correctamente.");# Finanzas AI
Sistema contable multimoneda con IA, ML y backend Java Spring Boot.

## Módulos:
- Frontend HTML listo para Vercel / GitHub Pages
- Java Spring Boot API
- Motor de ciencia de datos en Python
- Botones de pago PayPal, MercadoPago y tarjetas

## Deploy:
1. Subir carpeta completa a GitHub.
2. Conectar a Vercel → Deploy.
3. (Opcional) Activar GitHub Pages.<project xmlns="http://maven.apache.org/POM/4.0.0"  
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0  
         http://maven.apache.org/xsd/maven-4.0.0.xsd">  
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.finanzasai</groupId>
    <artifactId>finanzas-ai</artifactId>
    <version>1.0.0</version>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
</project>package com.finanzasai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class FinanzasAiApplication {
    public static void main(String[] args) {
        SpringApplication.run(FinanzasAiApplication.class, args);
    }
}package com.finanzasai.model;

public class AsientoRequest {
    public double montoARS;
    public double tipoCambioUSD;
    public double tipoCambioEUR;
    public double tipoCambioBRL;
    public double tipoCambioCLP;

    public double porcentajeIVA;
    public double pagoChequeTerceros;
    public double pagoPagares;

    public String fechaOperacion;
}package com.finanzasai.model;

public class AsientoResponse {
    public double montoUSD;
    public double montoEUR;
    public double montoBRL;
    public double montoCLP;

    public double ivaCalculado;
    public double totalConIVA;
    public double patrimonioNeto;
}package com.finanzasai.controller;

import com.finanzasai.model.AsientoRequest;
import com.finanzasai.model.AsientoResponse;
import com.finanzasai.service.AsientoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/asiento")
public class AsientoController {

    @Autowired
    private AsientoService asientoService;

    @PostMapping("/generar")
    public AsientoResponse generarAsiento(@RequestBody AsientoRequest request) {
        return asientoService.generarAsiento(request);
    }
}import pandas as pd
from sklearn.linear_model import LinearRegression

def predecir_cotizacion(datos):
    df = pd.DataFrame(datos)
    X = df[["inflacion", "base_monetaria", "tasas"]]
    y = df["dolar"]

    modelo = LinearRegression()
    modelo.fit(X, y)

    pred = modelo.predict([[100, 800000, 70]])
    return pred[0]