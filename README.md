!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>FINANZAS IA — App</title>
  <link rel="stylesheet" href="style.css" />

  <!-- Libs -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>

<body>

  <header class="site-header">
    <div class="brand">
      <div id="logo-placeholder">FINANZAS IA</div>
      <div class="tag">Tecnología + Análisis Financiero + IA</div>
    </div>
    <nav class="main-nav">
      <a href="#services">Servicios</a>
      <a href="#plans">Planes</a>
      <a href="#app">App</a>
      <a href="#contact">Contacto</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="app">
      <h1>Automatización contable con IA</h1>
      <p>Subí tu archivo CSV, mapeá columnas y generá asientos en segundos.</p>

      <div class="cta-row">
        <button id="btn-login" class="btn outline">Login / Register</button>
        <a class="btn primary" href="#contact">Contratar</a>
      </div>
    </section>

    <section class="section card">
      <h2>Cargar CSV</h2>

      <input id="file-input" type="file" accept=".csv" />

      <div id="preview-controls" class="cols hidden">
        <div><label>Monto</label><select id="col-amount"></select></div>
        <div><label>Descripción</label><select id="col-desc"></select></div>
        <div><label>Moneda</label><select id="col-curr"></select></div>
        <div><label>Tipo</label><select id="col-type"></select></div>
      </div>

      <div id="table-wrap" class="table-wrap hidden"></div>

      <div class="actions hidden" id="generate-row">
        <button id="generate-entries" class="btn primary">Generar Asientos</button>
      </div>
    </section>

    <section class="section card hidden" id="entries-section">
      <h2>Asientos generados</h2>

      <div id="entries-wrap"></div>

      <div class="actions">
        <button id="export-csv" class="btn">Exportar CSV</button>
        <button id="export-xlsx" class="btn">Exportar Excel</button>
        <button id="export-pdf" class="btn">Exportar PDF</button>
        <button id="download-original" class="btn outline">CSV original</button>
      </div>
    </section>

    <section class="section card" id="services">
      <h2>Servicios</h2>
      <ul>
        <li>Automatización contable con IA Generativa</li>
        <li>Modelos de anomalías</li>
        <li>Sistema multimoneda</li>
        <li>Dashboards financieros</li>
        <li>Integración API</li>
        <li>Consultoría profesional</li>
      </ul>
    </section>

    <section class="section card" id="plans">
      <h2>Planes</h2>
      <div class="plans">
        <div class="plan"><h3>Básico</h3><p>USD 300 / mes</p></div>
        <div class="plan highlighted"><h3>Pro</h3><p>USD 900 / mes</p></div>
        <div class="plan"><h3>Empresa</h3><p>USD 2000 / mes</p></div>
      </div>
    </section>

    <section class="section card" id="contact">
      <h2>Contacto</h2>
      <p>WhatsApp: 2613991663</p>
      <p>Email: priluskyezequielsamuel@gmail.com</p>
    </section>
  </main>

  <footer class="footer">
    © 2025 FINANZAS IA — Ezequiel S. Prilusky
  </footer>

  <script src="app.js"></script>
</body>
</html>               <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>FINANZAS IA — App</title>
  <link rel="stylesheet" href="style.css" />

  <!-- Libs -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>

<body>

  <header class="site-header">
    <div class="brand">
      <div id="logo-placeholder">FINANZAS IA</div>
      <div class="tag">Tecnología + Análisis Financiero + IA</div>
    </div>
    <nav class="main-nav">
      <a href="#services">Servicios</a>
      <a href="#plans">Planes</a>
      <a href="#app">App</a>
      <a href="#contact">Contacto</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="app">
      <h1>Automatización contable con IA</h1>
      <p>Subí tu archivo CSV, mapeá columnas y generá asientos en segundos.</p>

      <div class="cta-row">
        <button id="btn-login" class="btn outline">Login / Register</button>
        <a class="btn primary" href="#contact">Contratar</a>
      </div>
    </section>

    <section class="section card">
      <h2>Cargar CSV</h2>

      <input id="file-input" type="file" accept=".csv" />

      <div id="preview-controls" class="cols hidden">
        <div><label>Monto</label><select id="col-amount"></select></div>
        <div><label>Descripción</label><select id="col-desc"></select></div>
        <div><label>Moneda</label><select id="col-curr"></select></div>
        <div><label>Tipo</label><select id="col-type"></select></div>
      </div>

      <div id="table-wrap" class="table-wrap hidden"></div>

      <div class="actions hidden" id="generate-row">
        <button id="generate-entries" class="btn primary">Generar Asientos</button>
      </div>
    </section>

    <section class="section card hidden" id="entries-section">
      <h2>Asientos generados</h2>

      <div id="entries-wrap"></div>

      <div class="actions">
        <button id="export-csv" class="btn">Exportar CSV</button>
        <button id="export-xlsx" class="btn">Exportar Excel</button>
        <button id="export-pdf" class="btn">Exportar PDF</button>
        <button id="download-original" class="btn outline">CSV original</button>
      </div>
    </section>

    <section class="section card" id="services">
      <h2>Servicios</h2>
      <ul>
        <li>Automatización contable con IA Generativa</li>
        <li>Modelos de anomalías</li>
        <li>Sistema multimoneda</li>
        <li>Dashboards financieros</li>
        <li>Integración API</li>
        <li>Consultoría profesional</li>
      </ul>
    </section>

    <section class="section card" id="plans">
      <h2>Planes</h2>
      <div class="plans">
        <div class="plan"><h3>Básico</h3><p>USD 300 / mes</p></div>
        <div class="plan highlighted"><h3>Pro</h3><p>USD 900 / mes</p></div>
        <div class="plan"><h3>Empresa</h3><p>USD 2000 / mes</p></div>
      </div>
    </section>

    <section class="section card" id="contact">
      <h2>Contacto</h2>
      <p>WhatsApp: 2613991663</p>
      <p>Email: priluskyezequielsamuel@gmail.com</p>
    </section>
  </main>

  <footer class="footer">
    © 2025 FINANZAS IA — Ezequiel S. Prilusky
  </footer>

  <script src="app.js"></script>
</body>
</html>                 <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>FINANZAS IA — App</title>
  <link rel="stylesheet" href="style.css" />

  <!-- Libs -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>

<body>

  <header class="site-header">
    <div class="brand">
      <div id="logo-placeholder">FINANZAS IA</div>
      <div class="tag">Tecnología + Análisis Financiero + IA</div>
    </div>
    <nav class="main-nav">
      <a href="#services">Servicios</a>
      <a href="#plans">Planes</a>
      <a href="#app">App</a>
      <a href="#contact">Contacto</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="app">
      <h1>Automatización contable con IA</h1>
      <p>Subí tu archivo CSV, mapeá columnas y generá asientos en segundos.</p>

      <div class="cta-row">
        <button id="btn-login" class="btn outline">Login / Register</button>
        <a class="btn primary" href="#contact">Contratar</a>
      </div>
    </section>

    <section class="section card">
      <h2>Cargar CSV</h2>

      <input id="file-input" type="file" accept=".csv" />

      <div id="preview-controls" class="cols hidden">
        <div><label>Monto</label><select id="col-amount"></select></div>
        <div><label>Descripción</label><select id="col-desc"></select></div>
        <div><label>Moneda</label><select id="col-curr"></select></div>
        <div><label>Tipo</label><select id="col-type"></select></div>
      </div>

      <div id="table-wrap" class="table-wrap hidden"></div>

      <div class="actions hidden" id="generate-row">
        <button id="generate-entries" class="btn primary">Generar Asientos</button>
      </div>
    </section>

    <section class="section card hidden" id="entries-section">
      <h2>Asientos generados</h2>

      <div id="entries-wrap"></div>

      <div class="actions">
        <button id="export-csv" class="btn">Exportar CSV</button>
        <button id="export-xlsx" class="btn">Exportar Excel</button>
        <button id="export-pdf" class="btn">Exportar PDF</button>
        <button id="download-original" class="btn outline">CSV original</button>
      </div>
    </section>

    <section class="section card" id="services">
      <h2>Servicios</h2>
      <ul>
        <li>Automatización contable con IA Generativa</li>
        <li>Modelos de anomalías</li>
        <li>Sistema multimoneda</li>
        <li>Dashboards financieros</li>
        <li>Integración API</li>
        <li>Consultoría profesional</li>
      </ul>
    </section>

    <section class="section card" id="plans">
      <h2>Planes</h2>
      <div class="plans">
        <div class="plan"><h3>Básico</h3><p>USD 300 / mes</p></div>
        <div class="plan highlighted"><h3>Pro</h3><p>USD 900 / mes</p></div>
        <div class="plan"><h3>Empresa</h3><p>USD 2000 / mes</p></div>
      </div>
    </section>

    <section class="section card" id="contact">
      <h2>Contacto</h2>
      <p>WhatsApp: 2613991663</p>
      <p>Email: priluskyezequielsamuel@gmail.com</p>
    </section>
  </main>

  <footer class="footer">
    © 2025 FINANZAS IA — Ezequiel S. Prilusky
  </footer>

  <script src="app.js"></script>
</body>
</html>.             <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>FINANZAS IA — App</title>
  <link rel="stylesheet" href="style.css" />

  <!-- Libs -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>

<body>

  <header class="site-header">
    <div class="brand">
      <div id="logo-placeholder">FINANZAS IA</div>
      <div class="tag">Tecnología + Análisis Financiero + IA</div>
    </div>
    <nav class="main-nav">
      <a href="#services">Servicios</a>
      <a href="#plans">Planes</a>
      <a href="#app">App</a>
      <a href="#contact">Contacto</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="app">
      <h1>Automatización contable con IA</h1>
      <p>Subí tu archivo CSV, mapeá columnas y generá asientos en segundos.</p>

      <div class="cta-row">
        <button id="btn-login" class="btn outline">Login / Register</button>
        <a class="btn primary" href="#contact">Contratar</a>
      </div>
    </section>

    <section class="section card">
      <h2>Cargar CSV</h2>

      <input id="file-input" type="file" accept=".csv" />

      <div id="preview-controls" class="cols hidden">
        <div><label>Monto</label><select id="col-amount"></select></div>
        <div><label>Descripción</label><select id="col-desc"></select></div>
        <div><label>Moneda</label><select id="col-curr"></select></div>
        <div><label>Tipo</label><select id="col-type"></select></div>
      </div>

      <div id="table-wrap" class="table-wrap hidden"></div>

      <div class="actions hidden" id="generate-row">
        <button id="generate-entries" class="btn primary">Generar Asientos</button>
      </div>
    </section>

    <section class="section card hidden" id="entries-section">
      <h2>Asientos generados</h2>

      <div id="entries-wrap"></div>

      <div class="actions">
        <button id="export-csv" class="btn">Exportar CSV</button>
        <button id="export-xlsx" class="btn">Exportar Excel</button>
        <button id="export-pdf" class="btn">Exportar PDF</button>
        <button id="download-original" class="btn outline">CSV original</button>
      </div>
    </section>

    <section class="section card" id="services">
      <h2>Servicios</h2>
      <ul>
        <li>Automatización contable con IA Generativa</li>
        <li>Modelos de anomalías</li>
        <li>Sistema multimoneda</li>
        <li>Dashboards financieros</li>
        <li>Integración API</li>
        <li>Consultoría profesional</li>
      </ul>
    </section>

    <section class="section card" id="plans">
      <h2>Planes</h2>
      <div class="plans">
        <div class="plan"><h3>Básico</h3><p>USD 300 / mes</p></div>
        <div class="plan highlighted"><h3>Pro</h3><p>USD 900 / mes</p></div>
        <div class="plan"><h3>Empresa</h3><p>USD 2000 / mes</p></div>
      </div>
    </section>

    <section class="section card" id="contact">
      <h2>Contacto</h2>
      <p>WhatsApp: 2613991663</p>
      <p>Email: priluskyezequielsamuel@gmail.com</p>
    </section>
  </main>

  <footer class="footer">
    © 2025 FINANZAS IA — Ezequiel S. Prilusky
  </footer>

  <script src="app.js"></script>
</body>
</html>.                   :root{
  --bg:#0a1a33;
  --card:#0f2345;
  --accent:#3a5ed7;
  --muted:#9fb0df;
}

body{
  margin:0;
  background:var(--bg);
  color:white;
  font-family:Arial,sans-serif;
}

.site-header{
  display:flex;
  justify-content:space-between;
  padding:20px;
  border-bottom:1px solid #14243b;
}

.hero{
  text-align:center;
  padding:60px 20px;
}

.btn{
  padding:10px 16px;
  border-radius:8px;
  background:var(--accent);
  color:white;
  border:none;
  cursor:pointer;
}

.btn.outline{
  background:transparent;
  border:1px solid var(--accent);
}

.section{
  max-width:900px;
  margin:auto;
  padding:20px;
}

.card{
  background:var(--card);
  padding:20px;
  border-radius:12px;
  margin-bottom:20px;
}

.table-wrap{
  margin-top:20px;
  overflow:auto;
}

.cols{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:10px;
  margin-top:20px;
}

.hidden{display:none;}

.footer{
  text-align:center;
  padding:20px;
  color:var(--muted);
}.                    let originalData = null;

const fileInput = document.getElementById("file-input");
const previewControls = document.getElementById("preview-controls");
const tableWrap = document.getElementById("table-wrap");
const entriesWrap = document.getElementById("entries-wrap");
const entriesSection = document.getElementById("entries-section");

const selAmount = document.getElementById("col-amount");
const selDesc = document.getElementById("col-desc");
const selCurr = document.getElementById("col-curr");
const selType = document.getElementById("col-type");

fileInput.addEventListener("change", e => {
  const file = e.target.files[0];
  if (!file) return;

  Papa.parse(file, {
    header: true,
    skipEmptyLines: true,
    complete: (res) => {
      originalData = res.data;

      const headers = res.meta.fields || [];
      setupSelectors(headers);
      renderTable(originalData, headers);

      previewControls.classList.remove("hidden");
      document.getElementById("generate-row").classList.remove("hidden");
    }
  });
});

function setupSelectors(hdrs){
  [selAmount, selDesc, selCurr, selType].forEach(sel=>{
    sel.innerHTML = '<option value="">-- seleccionar --</option>';
    hdrs.forEach(h=>{
      let op = document.createElement("option");
      op.value = h;
      op.textContent = h;
      sel.appendChild(op);
    });
  });
}

function renderTable(data, headers){
  tableWrap.classList.remove("hidden");
  let html = "<table><thead><tr>";

  headers.forEach(h => html += `<th>${h}</th>`);
  html += "</tr></thead><tbody>";

  data.slice(0,200).forEach(row=>{
    html += "<tr>";
    headers.forEach(h=>{
      html += `<td>${row[h] || ""}</td>`;
    });
    html += "</tr>";
  });

  html += "</tbody></table>";
  tableWrap.innerHTML = html;
}

document.getElementById("generate-entries").addEventListener("click", ()=>{
  const amountCol = selAmount.value;
  const descCol = selDesc.value;
  const currCol = selCurr.value;
  const typeCol = selType.value;

  const entries = [];

  originalData.forEach(row=>{
    const amount = parseFloat(row[amountCol]?.replace(",",".") || 0);
    const desc = row[descCol] || "";
    const curr = row[currCol] || "";
    let type = row[typeCol]?.toLowerCase() || "";

    if(/vent/.test(type)) type = "venta";
    else if(/comp/.test(type)) type = "compra";
    else type = amount < 0 ? "compra" : "venta";

    entries.push({
      fecha: row["fecha"] || row["date"] || "",
      descripcion: desc,
      moneda: curr,
      debe: type === "venta" ? "Clientes" : "Gastos",
      haber: type === "venta" ? "Ingresos" : "Proveedores",
      monto: Math.abs(amount)
    });
  });

  window._generatedEntries = entries;
  renderEntries(entries);
  entriesSection.classList.remove("hidden");
});

function renderEntries(entries){
  entriesWrap.innerHTML = "";
  entries.forEach((e,i)=>{
    entriesWrap.innerHTML += `
      <div class="card">
        <strong>#${i+1}</strong> — ${e.fecha} (${e.moneda})
        <div><em>${e.descripcion}</em></div>
        <div>DEBE: ${e.debe} — ${e.monto}</div>
        <div>HABER: ${e.haber} — ${e.monto}</div>
      </div>
    `;
  });
}      