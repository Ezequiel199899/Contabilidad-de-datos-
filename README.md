PROYECTO COMPLETO: Contabilidad-de-datos- con IA integrada
====================================================================

Cada archivo empieza con una lÃ­nea ===== ARCHIVO: ruta =====
CopiÃ¡ el contenido entre esas lÃ­neas y creÃ¡ el archivo en GitHub
con esa misma ruta (Add file -> Create new file).


====================================================================
ARCHIVO: .env.example
====================================================================
# Clave de la API de Anthropic (Claude) - obligatoria para las consultas de IA
ANTHROPIC_API_KEY=tu_api_key_aca

# Opcional: proveedor externo de precios de materias primas
# (ej: metals-api.com, commodities-api.com). Sin esto, /materias-primas
# devuelve error 501 salvo que mandes tu propia serie de datos.
MATERIAS_PRIMAS_API_KEY=

# Base de datos (usada por Spring Boot)
DB_URL=jdbc:postgresql://localhost:5432/contabilidad
DB_USER=postgres
DB_PASSWORD=postgres


====================================================================
ARCHIVO: backend-flask/Dockerfile
====================================================================
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]


====================================================================
ARCHIVO: backend-flask/app.py
====================================================================
from flask import Flask, request, jsonify
import numpy as np
import os
import requests
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ---------- "Bases de datos" en memoria (reemplazar por PostgreSQL en producciÃ³n) ----------
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
    prompt = f"""Sos un {rol}. RespondÃ© en espaÃ±ol, claro y breve,
como lo harÃ­a un profesional explicÃ¡ndole a un dueÃ±o de PyME.

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
    contexto = f"Valores: {datos}\nPromedio: {avg:.2f} | Tendencia: {tendencia:.2f} | ProyecciÃ³n: {proyeccion:.2f}"
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
        return jsonify({"error": f"No existe la transacciÃ³n {tid}"}), 404
    if not pregunta:
        return jsonify({"error": "Falta 'pregunta'"}), 400

    contexto = f"TransacciÃ³n {tid}: monto={transaccion['monto']}, descripciÃ³n='{transaccion['descripcion']}'"
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
        return jsonify({"anomalias": [], "explicacion": "No se detectaron variaciones anÃ³malas."})

    contexto = f"Datos: {datos}\nAnomalÃ­as (z-score > 2): {anomalias}"
    explicacion = preguntar_ia(contexto, "ExplicÃ¡ brevemente por quÃ© estos valores son anÃ³malos y quÃ© revisar.")
    return jsonify({"anomalias": anomalias, "explicacion": explicacion})


# ======================================================================
# Divisas / tipos de cambio
# ======================================================================
def obtener_tipo_cambio(base, destino):
    """Usa Frankfurter (API pÃºblica, gratuita, sin key) para tipos de cambio de referencia."""
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
            return jsonify({"error": f"No se encontrÃ³ cotizaciÃ³n {base}->{destino}"}), 404
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
    Si hay MATERIAS_PRIMAS_API_KEY configurada, se puede reemplazar esta funciÃ³n por
    la llamada real a ese proveedor. Por ahora devuelve None si no hay key.
    """
    if not MATERIAS_PRIMAS_API_KEY:
        return None
    # Ejemplo de integraciÃ³n real (ajustar a la API que elijas):
    # r = requests.get(
    #     f"https://api.metals-api.com/v1/latest?access_key={MATERIAS_PRIMAS_API_KEY}&symbols={nombre}"
    # )
    # return r.json()["rates"][nombre]
    return None


@app.route("/materias-primas", methods=["GET"])
def ver_materia_prima():
    nombre = request.args.get("nombre", "").upper()
    if not nombre:
        return jsonify({"error": "Falta el parÃ¡metro 'nombre' (ej: XAU para oro, WTI para petrÃ³leo)"}), 400

    precio = obtener_precio_materia_prima(nombre)
    if precio is None:
        return jsonify({
            "error": "Sin proveedor de materias primas configurado",
            "detalle": "SeteÃ¡ MATERIAS_PRIMAS_API_KEY y conectÃ¡ tu proveedor en obtener_precio_materia_prima()"
        }), 501

    return jsonify({"nombre": nombre, "precio": precio})


@app.route("/ai/consultar-materias-primas", methods=["POST"])
def consultar_materias_primas():
    body = request.json
    pregunta = body.get("pregunta")
    nombre = body.get("nombre", "").upper()
    datos = body.get("datos")  # opcional: serie histÃ³rica que ya tenga el usuario

    if not pregunta:
        return jsonify({"error": "Falta 'pregunta'"}), 400

    if datos:
        avg, tendencia, proyeccion = calcular_metricas(datos)
        contexto = (
            f"Materia prima: {nombre or 'no especificada'}\n"
            f"Serie de precios: {datos}\n"
            f"Promedio: {avg:.2f} | Tendencia: {tendencia:.2f} | ProyecciÃ³n: {proyeccion:.2f}"
        )
    else:
        precio = obtener_precio_materia_prima(nombre) if nombre else None
        if precio is None:
            return jsonify({
                "error": "No hay precio disponible",
                "detalle": "PasÃ¡ 'datos' con una serie histÃ³rica, o configurÃ¡ MATERIAS_PRIMAS_API_KEY"
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


====================================================================
ARCHIVO: backend-flask/requirements.txt
====================================================================
flask==3.0.3
numpy==1.26.4
anthropic==0.34.2
gunicorn==22.0.0
requests==2.32.3


====================================================================
ARCHIVO: backend-spring/Dockerfile
====================================================================
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]


====================================================================
ARCHIVO: backend-spring/pom.xml
====================================================================
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.2</version>
        <relativePath/>
    </parent>

    <groupId>com.contabilidad</groupId>
    <artifactId>api</artifactId>
    <version>1.0.0</version>
    <name>api</name>
    <description>API principal - Plataforma de AnÃ¡lisis Financiero</description>

    <properties>
        <java.version>17</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <scope>runtime</scope>
        </dependency>

        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.5.0</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>


====================================================================
ARCHIVO: backend-spring/src/main/java/com/contabilidad/api/Application.java
====================================================================
package com.contabilidad.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}


====================================================================
ARCHIVO: backend-spring/src/main/java/com/contabilidad/api/controller/AiController.java
====================================================================
package com.contabilidad.api.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api/ai")
public class AiController {

    @Value("${flask.base-url:http://localhost:5000}")
    private String flaskBaseUrl;

    private final RestTemplate restTemplate;

    public AiController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // POST /api/ai/consultar -> reenvÃ­a a Flask /ai/consultar
    @PostMapping("/consultar")
    public ResponseEntity<Map> consultar(@RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/consultar";
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // POST /api/ai/consultar/{id} -> reenvÃ­a a Flask /ai/consultar/{id}
    @PostMapping("/consultar/{id}")
    public ResponseEntity<Map> consultarTransaccion(
            @PathVariable String id,
            @RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/consultar/" + id;
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // POST /api/ai/anomalias -> reenvÃ­a a Flask /ai/anomalias
    @PostMapping("/anomalias")
    public ResponseEntity<Map> anomalias(@RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/anomalias";
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // GET /api/ai/historial/{clave} -> reenvÃ­a a Flask /ai/historial/{clave}
    @GetMapping("/historial/{clave}")
    public ResponseEntity<Object[]> historial(@PathVariable String clave) {
        String url = flaskBaseUrl + "/ai/historial/" + clave;
        Object[] respuesta = restTemplate.getForObject(url, Object[].class);
        return ResponseEntity.ok(respuesta);
    }
}


====================================================================
ARCHIVO: backend-spring/src/main/java/com/contabilidad/api/controller/AnalyzeController.java
====================================================================
package com.contabilidad.api.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class AnalyzeController {

    @Value("${flask.base-url:http://localhost:5000}")
    private String flaskBaseUrl;

    private final RestTemplate restTemplate;

    public AnalyzeController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // GET /api/ -> health check
    @GetMapping("/")
    public ResponseEntity<Map<String, String>> health() {
        Map<String, String> status = new HashMap<>();
        status.put("status", "ok");
        status.put("service", "spring-boot");
        return ResponseEntity.ok(status);
    }

    // POST /api/analyze -> reenvÃ­a a Flask /forecast
    @PostMapping("/analyze")
    public ResponseEntity<Map> analyze(@RequestBody List<Map<String, Object>> movimientos) {
        List<Double> valores = movimientos.stream()
                .map(m -> Double.valueOf(m.get("amount").toString()))
                .toList();

        Map<String, Object> body = new HashMap<>();
        body.put("values", valores);

        String url = flaskBaseUrl + "/forecast";
        Map forecast = restTemplate.postForObject(url, body, Map.class);

        Map<String, Object> respuesta = new HashMap<>();
        respuesta.put("forecast", forecast);
        return ResponseEntity.ok(respuesta);
    }
}


====================================================================
ARCHIVO: backend-spring/src/main/java/com/contabilidad/api/controller/MercadoController.java
====================================================================
package com.contabilidad.api.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class MercadoController {

    @Value("${flask.base-url:http://localhos