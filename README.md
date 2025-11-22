

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

    <!-- SUBIDA DE CSV -->:root{
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

.footer{text-align:center;padding:12px;color:#777;}// Variables globales
let originalData = null;
let headers = [];

// Elementos del DOM
const fileInput = document.getElementById('file-input');
const previewControls = document.getElementById('preview-controls');
const previewSection = document.getElementById('preview-section');
const tableWrap = document.getElementById('table-wrap');
const entriesWrap = document.getElementById('entries-wrap');

const selAmount = document.getElementById('col-amount');
const selDesc = document.getElementById('col-desc');
const selCurr = document.getElementById('col-curr');
const selType = document.getElementById('col-type');

// Cargar CSV
fileInput.addEventListener("change", e => {
  const file = e.target.files[0];
  if (!file) return;

  Papa.parse(file, {
    header: true,
    skipEmptyLines: true,
    complete: (res) => {
      originalData = res.data;
      headers = res.meta.fields;

      if (!headers.length) {
        alert("El CSV no tiene encabezados.");
        return;
      }

      setupSelectors(headers);
      renderTable(originalData, headers);

      previewControls.classList.remove("hidden");
      previewSection.classList.remove("hidden");
    }
  });
});

// Rellenar selects
function setupSelectors(hdrs){
  [selAmount, selDesc, selCurr, selType].forEach(sel=>{
    sel.innerHTML = '<option value="">-- elegir --</option>';
    hdrs.forEach(h=>{
      let op = document.createElement("option");
      op.value = h; op.textContent = h;
      sel.appendChild(op);
    });
  });
}

// Tabla de preview
function renderTable(data, hdrs){
  let html = `<table><thead><tr>`;
  hdrs.forEach(h=> html += `<th>${h}</th>`);
  html += `</tr></thead><tbody>`;

  data.slice(0,200).forEach(row=>{
    html += `<tr>`;
    hdrs.forEach(h=>{
      html += `<td>${row[h] ?? ""}</td>`;
    });
    html += `</tr>`;
  });

  html += `</tbody></table>`;
  tableWrap.innerHTML = html;
}

// Generar Asientos
document.getElementById("generate-entries").addEventListener("click", ()=>{

  const A = selAmount.value;
  const D = selDesc.value;
  const C = selCurr.value;
  const T = selType.value;

  const entries = [];

  originalData.forEach(row=>{

    const monto = parseFloat(String(row[A] || "0").replace(",", ".")) || 0;
    const desc  = row[D] || "";
    const curr  = row[C] || "";
    let tipo    = row[T] ? row[T].toLowerCase() : "";

    // heurística básica
    if (/comp/.test(tipo)) tipo="compra";
    else if (/vent|ingr/.test(tipo)) tipo="venta";
    else tipo = monto < 0 ? "compra" : "venta";

    entries.push({
      fecha: row["date"] || row["fecha"] || "",
      descripcion: desc,
      moneda: curr,
      debe_cuenta: tipo==="venta" ? "Clientes" : "Gastos",
      haber_cuenta: tipo==="venta" ? "Ingresos" : "Proveedores",
      monto: Math.abs(monto)
    });
  });

  window._generatedEntries = entries;
  renderEntries(entries);
});

// Render entries
function renderEntries(entries){
  entriesWrap.innerHTML = "";
  entries.forEach((e,i)=>{
    entriesWrap.innerHTML += `
      <div class="entry">
        <strong>#${i+1}</strong>
        <div>${e.fecha} — ${e.moneda}</div>
        <div><em>${e.descripcion}</em></div>
        <div>DEBE: ${e.debe_cuenta} — ${e.monto}</div>
        <div>HABER: ${e.haber_cuenta} — ${e.monto}</div>
      </div>
    `;
  });
}

// EXPORTS
document.getElementById("export-csv").addEventListener("click", ()=>{
  let e = window._generatedEntries || [];
  if (!e.length) return alert("No hay asientos.");

  const headers = ["fecha","descripcion","moneda","debe_cuenta","haber_cuenta","monto"];
  const csv = [headers.join(",")]
    .concat(e.map(r => headers.map(h => `"${r[h]}"`).join(",")))
    .join("\n");

  downloadFile("asientos.csv", csv, "text/csv");
});

document.getElementById("export-xlsx").addEventListener("click", ()=>{
  let e = window._generatedEntries || [];
  if (!e.length) return alert("No hay asientos.");

  const ws = XLSX.utils.json_to_sheet(e);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Asientos");
  XLSX.writeFile(wb, "asientos.xlsx");
});

document.getElementById("export-pdf").addEventListener("click", ()=>{
  let e = window._generatedEntries || [];
  if (!e.length) return alert("No hay asientos.");

  const { jsPDF } = window.jspdf;
  const pdf = new jsPDF();
  const rows = e.map((r,i)=>[i+1, r.fecha, r.descripcion, r.moneda, r.debe_cuenta, r.haber_cuenta, r.monto]);

  pdf.text("Asientos Contables — Finanzas AI", 10, 10);
  pdf.autoTable({
    head:[["#","Fecha","Descripcion","Moneda","Debe","Haber","Monto"]],
    body:rows,
    startY:20
  });

  pdf.save("asientos.pdf");
});

// Descargar archivo helper
function downloadFile(name, data, type){
  const blob = new Blob([data], {type});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = name;
  a.click();
  URL.revokeObjectURL(url);
}document.getElementById("run-ai").addEventListener("click", ()=>{

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