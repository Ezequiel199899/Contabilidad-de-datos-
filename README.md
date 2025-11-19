<!DOCTYPE html>
<html>
<head>  
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finanzas AI – Sistema Contable Multimoneda</title>  
    <link rel="stylesheet" href="style.css">  
</head>  
<body>  
    <header>
        <h1>Finanzas AI</h1>  
        <h3>Asientos Contables Predictivos con Machine Learning</h3>  
        <p>Demostración del Sistema Bimonetario Inteligente</p>
    </header>

    <section id="upload-section">
        <h2>Cargar Archivo de Transacciones (CSV)</h2>
        <p>Sube tu archivo para que la IA clasifique y genere los asientos.</p>
        
        <input type="file" id="csvFileInput" accept=".csv" class="file-input">
        
        <button id="processButton">
            Procesar y Generar Asientos
        </button>

        <div id="statusMessage"></div>
    </section>

    <section id="results-section" style="display:none;">
        <h2>Resultados del Procesamiento</h2>
        <table id="asientoTable">
            <thead>
                <tr>
                    <th>Descripción</th>
                    <th>Monto ARS</th>
                    <th>Cuenta DEBE (IA)</th>
                    <th>Cuenta HABER (IA)</th>
                    <th>Ajuste Predictivo</th>
                </tr>
            </thead>
            <tbody>
                </tbody>
        </table>
    </section>
    
    <script src="app.js"></script>  
</body>  
</html>
body {  
    font-family: Arial, sans-serif;  
    padding: 40px;  
    background: #f1f1f1;  
    max-width: 800px;
    margin: 0 auto;
}  

h1, h2, h3 {
    color: #004a8f;
}

button {
    padding: 12px 20px;
    border-radius: 8px;
    border: none;
    background: #0070f3;
    color: white;
    margin-top: 15px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.3s;
}

button:hover {
    background: #0056b3;
}

.file-input {
    display: block;
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#statusMessage {
    margin-top: 20px;
    font-weight: bold;
    color: #4CAF50; /* Verde para éxito */
}

/* Estilo básico de tabla para resultados */
#asientoTable {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}
#asientoTable th, #asientoTable td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
#asientoTable th {
    background-color: #e9e9e9;
}
console.log("Finanzas AI app cargada correctamente.");

document.getElementById('processButton').addEventListener('click', function() {
    const fileInput = document.getElementById('csvFileInput');
    const statusMessage = document.getElementById('statusMessage');
    const resultsSection = document.getElementById('results-section');
    const tableBody = document.querySelector('#asientoTable tbody');

    if (fileInput.files.length === 0) {
        statusMessage.textContent = "Por favor, selecciona un archivo CSV.";
        statusMessage.style.color = '#FF9800'; // Naranja para advertencia
        resultsSection.style.display = 'none';
        return;
    }

    statusMessage.textContent = "Procesando archivo... contactando Motor de IA...";
    statusMessage.style.color = '#0070f3'; // Azul para progreso
    resultsSection.style.display = 'none';
    tableBody.innerHTML = ''; // Limpiar resultados anteriores

    // --- SIMULACIÓN DE LLAMADA AL BACKEND (Motor de IA) ---
    // NOTA: Cuando el Backend esté desplegado, esta simulación debe ser reemplazada por una llamada "fetch" real.
    setTimeout(() => {
        const simulatedResults = [
            {
                descripcion: "Venta de productos a cliente A",
                montoARS: 10000.00,
                cuentaDebe: "Clientes",
                cuentaHaber: "Ventas",
                ajustePredictivo: 55.20 
            },
            {
                descripcion: "Compra de insumos de oficina",
                montoARS: 2500.50,
                cuentaDebe: "Gastos Administrativos",
                cuentaHaber: "Caja",
                ajustePredictivo: 0.00 
            }
        ];

        simulatedResults.forEach(asiento => {
            const row = tableBody.insertRow();
            row.insertCell().textContent = asiento.descripcion;
            row.insertCell().textContent = `$${asiento.montoARS.toFixed(2)}`;
            row.insertCell().textContent = asiento.cuentaDebe;
            row.insertCell().textContent = asiento.cuentaHaber;
            row.insertCell().textContent = `$${asiento.ajustePredictivo.toFixed(2)}`;
        });
        
        statusMessage.textContent = "✅ Proceso completado. Asientos generados y clasificados por la IA.";
        statusMessage.style.color = '#4CAF50';
        resultsSection.style.display = 'block';

    }, 3000); // Espera 3 segundos para simular el procesamiento de la IA
});
body {  
    font-family: Arial, sans-serif;  
    padding: 40px;  
    background: #f1f1f1;  
    max-width: 800px;
    margin: 0 auto;
}  

h1, h2, h3 {
    color: #004a8f;
}

button {
    padding: 12px 20px;
    border-radius: 8px;
    border: none;
    background: #0070f3;
    color: white;
    margin-top: 15px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.3s;
}

button:hover {
    background: #0056b3;
}

.file-input {
    display: block;
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#statusMessage {
    margin-top: 20px;
    font-weight: bold;
    color: #4CAF50; /* Verde para éxito */
}

/* Estilo básico de tabla para resultados */
#asientoTable {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}
#asientoTable th, #asientoTable td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
#asientoTable th {
    background-color: #e9e9e9;
}
console.log("Finanzas AI app cargada correctamente.");

document.getElementById('processButton').addEventListener('click', function() {
    const fileInput = document.getElementById('csvFileInput');
    const statusMessage = document.getElementById('statusMessage');
    const resultsSection = document.getElementById('results-section');
    const tableBody = document.querySelector('#asientoTable tbody');

    if (fileInput.files.length === 0) {
        statusMessage.textContent = "Por favor, selecciona un archivo CSV.";
        statusMessage.style.color = '#FF9800'; // Naranja para advertencia
        resultsSection.style.display = 'none';
        return;
    }

    statusMessage.textContent = "Procesando archivo... contactando Motor de IA...";
    statusMessage.style.color = '#0070f3'; // Azul para progreso
    resultsSection.style.display = 'none';
    tableBody.innerHTML = ''; // Limpiar resultados anteriores

    // --- SIMULACIÓN DE LLAMADA AL BACKEND (Motor de IA) ---
    // NOTA: Cuando el Backend esté desplegado, esta simulación debe ser reemplazada por una llamada "fetch" real.
    setTimeout(() => {
        const simulatedResults = [
            {
                descripcion: "Venta de productos a cliente A",
                montoARS: 10000.00,
                cuentaDebe: "Clientes",
                cuentaHaber: "Ventas",
                ajustePredictivo: 55.20 
            },
            {
                descripcion: "Compra de insumos de oficina",
                montoARS: 2500.50,
                cuentaDebe: "Gastos Administrativos",
                cuentaHaber: "Caja",
                ajustePredictivo: 0.00 
            }
        ];

        simulatedResults.forEach(asiento => {
            const row = tableBody.insertRow();
            row.insertCell().textContent = asiento.descripcion;
            row.insertCell().textContent = `$${asiento.montoARS.toFixed(2)}`;
            row.insertCell().textContent = asiento.cuentaDebe;
            row.insertCell().textContent = asiento.cuentaHaber;
            row.insertCell().textContent = `$${asiento.ajustePredictivo.toFixed(2)}`;
        });
        
        statusMessage.textContent = "✅ Proceso completado. Asientos generados y clasificados por la IA.";
        statusMessage.style.color = '#4CAF50';
        resultsSection.style.display = 'block';

    }, 3000); // Espera 3 segundos para simular el procesamiento de la IA
});
<project xmlns="http://maven.apache.org/POM/4.0.0"    
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

</project>
package com.finanzasai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class FinanzasAiApplication {
    public static void main(String[] args) {
        SpringApplication.run(FinanzasAiApplication.class, args);
    }
}
package com.finanzasai.model;

public class AsientoRequest {
    public double montoARS;
    public double tipoCambioUSD;
    public double porcentajeIVA;  
    
    public String fechaOperacion;
    public String descripcionOperacion; // CLAVE: usada por el motor de IA
    public String monedaOrigen;         
}
package com.finanzasai.model;

public class AsientoResponse {
    public String cuentaDebe;
    public String cuentaHaber;
    public double montoDebe;
    public double montoHaber;
    
    public double ivaCalculado;  
    public double diferenciaTipoCambioReal;
    public double ajustePredictivoRevaluo; // CLAVE: Sugerido por ML para provisiones
    public String sugerenciaClasificacionML;
}
package com.finanzasai.controller;

import com.finanzasai.model.AsientoRequest;
import com.finanzasai.model.AsientoResponse;
// Importaciones requeridas para el manejo de archivos y servicios
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import java.util.List;
import com.finanzasai.service.AsientoService; // Asumiendo que existe un AsientoService

@RestController
@RequestMapping("/api/asiento")
public class AsientoController {

    // @Autowired  
    // private AsientoService asientoService; // Descomentar al implementar el servicio real

    @PostMapping("/generar")  
    public AsientoResponse generarAsiento(@RequestBody AsientoRequest request) {  
        // Lógica de generación de un solo asiento
        return new AsientoResponse(); // Retorna un objeto simulado
    }

    @PostMapping("/upload-csv")
    public List<AsientoResponse> procesarCSV(@RequestParam("file") MultipartFile file) {
        // Endpoint clave para la carga de archivos CSV
        // La lógica real llamaría al servicio que interactúa con el motor de Python
        return List.of(new AsientoResponse()); // Retorna una lista de objetos simulados
    }
}

