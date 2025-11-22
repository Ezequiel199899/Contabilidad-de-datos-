 
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Finanzas AI – Sistema Contable Multimoneda</title>
  <link rel="stylesheet" href="style.css" />

  <!-- Librerías externas -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>

<body>
  <header class="header">
    <h1>Finanzas AI</h1>
    <h3>Asientos Contables Predictivos con IA</h3>
    <p>Sistema Multimoneda – Prototipo listo para demo</p>
  </header>

  <main class="container">

    <!-- SUBIDA DE CSV -->
    <section class="card">
      <h2>Cargar Archivo CSV</h2>
      <input id="file-input" type="file" accept=".csv">

      <div id="preview-controls" class="hidden">

        <label>Columna Monto:</label>
        <select id="col-amount"></select>

        <label>Columna Descripción:</label>
        <select id="col-desc"></select>

        <label>Columna Moneda:</label>
        <select id="col-curr"></select>

        <label>Columna Tipo:</label>
        <select id="col-type"></select>

        <button id="generate-entries">Generar Asientos</button>
      </div>
    </section>

    <!-- PREVIEW TABLA + ASIENTOS -->
    <section id="preview-section" class="card hidden">
      <h2>Transacciones detectadas</h2>
      <div id="table-wrap"></div>

      <h3>Asientos generados</h3>
      <div id="entries-wrap"></div>

      <div class="actions">
        <button id="export-csv">Exportar CSV</button>
        <button id="export-xlsx">Exportar Excel</button>
        <button id="export-pdf">Exportar PDF</button>
        <button id="download-original" class="secondary">Descargar Original</button>
      </div>
    </section>

    <!-- IA GENERATIVA -->
    <section class="card">
      <h2>Análisis Inteligente (IA Generativa)</h2>
      <button id="run-ai">Analizar con IA</button>
      <div id="ai-output" class="ai-box"></div>
    </section>

  </main>

  <footer class="footer">
    <small>Finanzas AI © Prototipo | Listo para GitHub Pages</small>
  </footer>

  <script src="script.js"></script>
  <script src="ia.js"></script>
</body>
</html>.       :root{
  --bg:#f6f8fb;
  --card:#ffffff;
  --accent:#1f6feb;
  --muted:#666;
  --radius:12px;
  --pad:14px;
}
*{box-sizing:border-box;font-family:Inter,Arial,sans-serif;}

body{
  margin:0;background:var(--bg);color:#0d1a2b;
}

.header{
  padding:18px;background:#eef4ff;border-bottom:1px solid #dde5ff;text-align:center;
}

.container{max-width:960px;margin:20px auto;padding:10px;}

.card{
  background:var(--card);padding:var(--pad);
  border-radius:var(--radius);box-shadow:0 4px 16px #0001;
  margin-bottom:20px;
}

input[type=file]{margin:12px 0;}

select{
  width:100%;padding:8px;margin-bottom:10px;
  border-radius:8px;border:1px solid #ddd;
}

button{
  background:var(--accent);color:white;border:0;
  border-radius:8px;padding:10px 14px;cursor:pointer;
  margin-top:10px;
}
button.secondary{background:#e7ecff;color:#0d1a2b;}

.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;}

.hidden{display:none;}

#table-wrap{
  overflow:auto;max-height:250px;
  border:1px solid #eef; padding:8px;border-radius:8px;
}

table{width:100%;border-collapse:collapse;font-size:13px;}
th,td{padding:6px 8px;border-bottom:1px solid #f0f4ff;}
th{background:#f6f9ff;position:sticky;top:0;}

.entry{
  border:1px dashed #dde;border-radius:8px;padding:10px;
  margin-bottom:10px;
}

.ai-box{
  background:#f7faff;border:1px solid #dce6ff;
  padding:14px;border-radius:8px;margin-top:12px;
  white-space:pre-wrap;
}

.footer{text-align:center;padding:12px;color:#777;}.      document.getElementById("run-ai").addEventListener("click", ()=>{

  if (!originalData){
    return alert("Subí un CSV primero.");
  }

  const resumen = generarResumen(originalData);
  const mensaje = `
📊 Análisis IA Generativa — DEMO LOCAL
---------------------------------------

Total de transacciones: ${resumen.total}
Monto promedio: ${resumen.promedio.toFixed(2)}
Monto máximo: ${resumen.max.toFixed(2)}
Monedas detectadas: ${resumen.monedas.join(", ")}

🧠 Sugerencias contables automáticas:
- Detecto ${resumen.pagos_grandes} pagos inusualmente grandes.
- Las ventas superiores a ARS 50.000 pueden requerir asiento compuesto.
- Los gastos pequeños son consistentes y podrían agruparse.
- Se pueden clasificar automáticamente: compras, ventas, servicios y misceláneos.

💡 Nota:
Esta IA está en modo DEMO (sin servidor).
Si querés la versión real conectada a OpenAI o Gemini → te la preparo.
  `;

  document.getElementById("ai-output").textContent = mensaje;
});

function generarResumen(data){
  const montos = data.map(r => parseFloat(String(r.amount || r.monto || 0).replace(",", ".")) || 0);

  return {
    total: data.length,
    promedio: montos.reduce((a,b)=>a+b,0)/montos.length,
    max: Math.max(...montos),
    monedas: [...new Set(data.map(r => r.currency || r.moneda || "N/A"))],
    pagos_grandes: montos.filter(v => v > 50000).length
  };
}.               document.getElementById("run-ai").addEventListener("click", ()=>{

  if (!originalData){
    return alert("Subí un CSV primero.");
  }

  const resumen = generarResumen(originalData);
  const mensaje = `
📊 Análisis IA Generativa — DEMO LOCAL
---------------------------------------

Total de transacciones: ${resumen.total}
Monto promedio: ${resumen.promedio.toFixed(2)}
Monto máximo: ${resumen.max.toFixed(2)}
Monedas detectadas: ${resumen.monedas.join(", ")}

🧠 Sugerencias contables automáticas:
- Detecto ${resumen.pagos_grandes} pagos inusualmente grandes.
- Las ventas superiores a ARS 50.000 pueden requerir asiento compuesto.
- Los gastos pequeños son consistentes y podrían agruparse.
- Se pueden clasificar automáticamente: compras, ventas, servicios y misceláneos.

💡 Nota:
Esta IA está en modo DEMO (sin servidor).
Si querés la versión real conectada a OpenAI o Gemini → te la preparo.
  `;

  document.getElementById("ai-output").textContent = mensaje;
});

function generarResumen(data){
  const montos = data.map(r => parseFloat(String(r.amount || r.monto || 0).replace(",", ".")) || 0);

  return {
    total: data.length,
    promedio: montos.reduce((a,b)=>a+b,0)/montos.length,
    max: Math.max(...montos),
    monedas: [...new Set(data.map(r => r.currency || r.moneda || "N/A"))],
    pagos_grandes: montos.filter(v => v > 50000).length
  };
}