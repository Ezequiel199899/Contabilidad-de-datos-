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

    @Value("${flask.base-url:http://localhost:5000}")
    private String flaskBaseUrl;

    private final RestTemplate restTemplate;

    public MercadoController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // ---------- Divisas ----------

    // GET /api/divisas?base=USD&destino=EUR -> Flask /divisas
    @GetMapping("/divisas")
    public ResponseEntity<Map> verDivisa(
            @RequestParam(defaultValue = "USD") String base,
            @RequestParam(defaultValue = "EUR") String destino) {
        String url = flaskBaseUrl + "/divisas?base=" + base + "&destino=" + destino;
        Map respuesta = restTemplate.getForObject(url, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // POST /api/ai/consultar-divisas -> Flask /ai/consultar-divisas
    @PostMapping("/ai/consultar-divisas")
    public ResponseEntity<Map> consultarDivisas(@RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/consultar-divisas";
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // ---------- Materias primas ----------

    // GET /api/materias-primas?nombre=XAU -> Flask /materias-primas
    @GetMapping("/materias-primas")
    public ResponseEntity<Map> verMateriaPrima(@RequestParam String nombre) {
        String url = flaskBaseUrl + "/materias-primas?nombre=" + nombre;
        Map respuesta = restTemplate.getForObject(url, Map.class);
        return ResponseEntity.ok(respuesta);
    }

    // POST /api/ai/consultar-materias-primas -> Flask /ai/consultar-materias-primas
    @PostMapping("/ai/consultar-materias-primas")
    public ResponseEntity<Map> consultarMateriasPrimas(@RequestBody Map<String, Object> body) {
        String url = flaskBaseUrl + "/ai/consultar-materias-primas";
        Map respuesta = restTemplate.postForObject(url, body, Map.class);
        return ResponseEntity.ok(respuesta);
    }
}


====================================================================
ARCHIVO: backend-spring/src/main/resources/application.properties
====================================================================
server.port=8080

# URL del microservicio Flask (forecasting + IA)
flask.base-url=${FLASK_BASE_URL:http://localhost:5000}

# Base de datos PostgreSQL
spring.datasource.url=${DB_URL:jdbc:postgresql://localhost:5432/contabilidad}
spring.datasource.username=${DB_USER:postgres}
spring.datasource.password=${DB_PASSWORD:postgres}
spring.jpa.hibernate.ddl-auto=update

# Swagger / OpenAPI en /docs
springdoc.swagger-ui.path=/docs


====================================================================
ARCHIVO: docker-compose.yml
====================================================================
version: "3.9"

services:
  backend-flask:
    build: ./backend-flask
    ports:
      - "5000:5000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - PORT=5000

  backend-spring:
    build: ./backend-spring
    ports:
      - "8080:8080"
    environment:
      - FLASK_BASE_URL=http://backend-flask:5000
      - DB_URL=jdbc:postgresql://db:5432/contabilidad
      - DB_USER=postgres
      - DB_PASSWORD=postgres
    depends_on:
      - backend-flask
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=contabilidad
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
