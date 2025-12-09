# Finanzas IA — Enterprise Edition
Autor: Ezequiel Samuel Prilusky
Fecha: 27 de noviembre de 2025
Estado: Privado - listo para despliegue (frontend + backend)

Resumen
-------
Versión empresarial del prototipo “Finanzas IA”. Contiene:
- Frontend estático (HTML/CSS/JS) para carga CSV y UI.
- Backend en FastAPI con autenticación JWT, endpoints protegidos y predicción stub.
- Estructura lista para Docker y despliegue en Render/Vercel.

Instrucciones rápidas
---------------------
1. Subir repo privado a GitHub.
2. Añadir secretos (JWT_SECRET, ALLOWED_HOSTS, DATABASE_URL) en la plataforma de despliegue.
3. Desplegar frontend en Vercel / GitHub Pages (carpeta `frontend/`).
4. Desplegar backend como servicio web en Render / Heroku / AWS (carpeta `backend/`).

Contacto
--------
Ezequiel Samuel Prilusky
Email: priluskyezequielsamuel@gmail.com
WhatsApp: +54 261 399 1663.        
__pycache__/
*.pyc
.env
venv/
backend/finanzas.db
.DS_Store
node_modules/
.vscode/.          <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>FINANZAS IA — App</title>
  <link rel="stylesheet" href="style.css" />
  <meta name="description" content="Finanzas IA - Automatización contable con IA" />
  <!-- Libs -->
  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>
<body>
  <header class="site-header">
    <div class="brand">
      <img src="assets/logo.png" alt="Finanzas IA" id="logo" />
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
        <li>Modelos de detección de anomalías</li>
        <li>Sistema multimoneda y reportes</li>
        <li>Dashboards financieros</li>
        <li>Integración API / Consultoría</li>
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
      <p>WhatsApp: <a href="https://wa.me/5492613991663" target="_blank">+54 9 261 399 1663</a></p>
      <p>Email: <a href="mailto:priluskyezequielsamuel@gmail.com">priluskyezequielsamuel@gmail.com</a></p>
    </section>
  </main>

  <footer class="footer">
    © 2025 FINANZAS IA — Ezequiel S. Prilusky
  </footer>

  <script src="app.js"></script>
</body>
</html>.         
.           :root{
  --bg:#0a1a33;
  --card:#0f2345;
  --accent:#163f8a; /* azul tech más serio */
  --muted:#9fb0df;
  --pad:18px;
}
*{box-sizing:border-box;font-family:Inter,Arial,sans-serif}
body{margin:0;background:var(--bg);color:#fff}
.site-header{display:flex;justify-content:space-between;align-items:center;padding:14px 24px;border-bottom:1px solid #14243b}
.brand{display:flex;flex-direction:row;gap:12px;align-items:center}
.brand img#logo{height:48px}
.tag{font-size:12px;color:var(--muted)}
.main-nav a{color:#cfe1ff;margin-left:12px;text-decoration:none}
.hero{padding:48px 20px;text-align:center}
.hero h1{font-size:32px;margin:0 0 6px;font-style:italic}
.card{background:var(--card);padding:var(--pad);border-radius:12px;margin:20px auto;max-width:1000px}
.cols{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px}
.table-wrap{overflow:auto;max-height:320px;border-radius:8px;padding:8px;margin-top:12px}
.btn{background:var(--accent);color:white;padding:10px 14px;border-radius:8px;border:0;cursor:pointer}
.btn.outline{background:transparent;border:1px solid rgba(255,255,255,0.08)}
.plans{display:flex;gap:12px;flex-wrap:wrap}
.plan{flex:1;background:#102444;padding:18px;border-radius:10px;text-align:center}
.plan.highlighted{border:2px solid var(--accent);transform:scale(1.02)}
.footer{text-align:center;padding:20px;color:var(--muted)}
.hidden{display:none}
@media(max-width:880px){.cols{grid-template-columns:repeat(2,1fr)}.plans{flex-direction:column}}.         :root{
  --bg:#0a1a33;
  --card:#0f2345;
  --accent:#163f8a; /* azul tech más serio */
  --muted:#9fb0df;
  --pad:18px;
}
*{box-sizing:border-box;font-family:Inter,Arial,sans-serif}
body{margin:0;background:var(--bg);color:#fff}
.site-header{display:flex;justify-content:space-between;align-items:center;padding:14px 24px;border-bottom:1px solid #14243b}
.brand{display:flex;flex-direction:row;gap:12px;align-items:center}
.brand img#logo{height:48px}
.tag{font-size:12px;color:var(--muted)}
.main-nav a{color:#cfe1ff;margin-left:12px;text-decoration:none}
.hero{padding:48px 20px;text-align:center}
.hero h1{font-size:32px;margin:0 0 6px;font-style:italic}
.card{background:var(--card);padding:var(--pad);border-radius:12px;margin:20px auto;max-width:1000px}
.cols{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px}
.table-wrap{overflow:auto;max-height:320px;border-radius:8px;padding:8px;margin-top:12px}
.btn{background:var(--accent);color:white;padding:10px 14px;border-radius:8px;border:0;cursor:pointer}
.btn.outline{background:transparent;border:1px solid rgba(255,255,255,0.08)}
.plans{display:flex;gap:12px;flex-wrap:wrap}
.plan{flex:1;background:#102444;padding:18px;border-radius:10px;text-align:center}
.plan.highlighted{border:2px solid var(--accent);transform:scale(1.02)}
.footer{text-align:center;padding:20px;color:var(--muted)}
.hidden{display:none}
@media(max-width:880px){.cols{grid-template-columns:repeat(2,1fr)}.plans{flex-direction:column}}.      // frontend/app.js - UX + demo integration with backend
let originalData = null;
const fileInput = document.getElementById('file-input');
const previewControls = document.getElementById('preview-controls');
const tableWrap = document.getElementById('table-wrap');
const entriesWrap = document.getElementById('entries-wrap');
const entriesSection = document.getElementById('entries-section');
const selAmount = document.getElementById('col-amount');
const selDesc = document.getElementById('col-desc');
const selCurr = document.getElementById('col-curr');
const selType = document.getElementById('col-type');

fileInput && fileInput.addEventListener('change', e=>{
  const file = e.target.files[0]; if(!file) return;
  Papa.parse(file, {
    header: true, skipEmptyLines: true,
    complete: (res)=>{
      originalData = res.data;
      const headers = res.meta.fields || [];
      setupSelectors(headers);
      renderTable(originalData, headers);
      previewControls.classList.remove('hidden');
      document.getElementById('generate-row').classList.remove('hidden');
    }
  });
});

function setupSelectors(hdrs){
  [selAmount, selDesc, selCurr, selType].forEach(sel=>{
    sel.innerHTML = '<option value="">-- seleccionar --</option>';
    hdrs.forEach(h=>{
      const op = document.createElement('option');
      op.value = h; op.textContent = h;
      sel.appendChild(op);
    });
  });
}

function renderTable(data, headers){
  tableWrap.classList.remove('hidden');
  let html = '<table><thead><tr>';
  headers.forEach(h => html += `<th>${h}</th>`);
  html += '</tr></thead><tbody>';
  data.slice(0,200).forEach(row=>{
    html += '<tr>';
    headers.forEach(h => html += `<td>${row[h] ?? ''}</td>`);
    html += '</tr>';
  });
  html += '</tbody></table>';
  tableWrap.innerHTML = html;
}

document.getElementById('generate-entries')?.addEventListener('click', ()=>{
  if(!originalData) return alert('Subí un CSV primero.');
  const A = selAmount.value; const D = selDesc.value; const C = selCurr.value; const T = selType.value;
  const entries = [];
  originalData.forEach(r=>{
    const raw = A ? r[A] : (r.amount || r.monto || r.importe || 0);
    let v = String(raw).replace(/[^0-9\-\.,]/g,'').replace(',','.');
    const amount = parseFloat(v) || 0;
    const desc = D ? r[D] : (r.description||r.detalle||'');
    const curr = C ? r[C] : (r.currency||r.moneda||'');
    let tipo = T ? String(r[T]||'').toLowerCase() : (amount < 0 ? 'compra' : 'venta');
    if(/comp|buy|purchase/i.test(tipo)) tipo='compra';
    else if(/ven|sale|ingr|invoice|venta/i.test(tipo)) tipo='venta';
    else tipo = amount < 0 ? 'compra' : 'venta';
    if(amount === 0) return;
    if(tipo === 'venta'){
      entries.push({fecha: r.date || r.fecha || '', descripcion: desc, moneda: curr, debe: 'Clientes', haber: 'Ingresos', monto: Math.abs(amount)});
    } else {
      entries.push({fecha: r.date || r.fecha || '', descripcion: desc, moneda: curr, debe: 'Gastos', haber: 'Proveedores', monto: Math.abs(amount)});
    }
  });
  window._generatedEntries = entries;
  renderEntries(entries);
  entriesSection.classList.remove('hidden');
});

function renderEntries(entries){
  entriesWrap.innerHTML = '';
  if(!entries.length){ entriesWrap.innerHTML = 'No se generaron asientos.'; return; }
  entries.forEach((e,i)=>{
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `<strong>#${i+1}</strong> — ${e.fecha} (${e.moneda})<div><em>${e.descripcion}</em></div><div>DEBE: ${e.debe} — ${e.monto}</div><div>HABER: ${e.haber} — ${e.monto}</div>`;
    entriesWrap.appendChild(div);
  });
}

// Export helpers
function downloadFile(name, data, type='text/plain'){
  const blob = new Blob([data], {type});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url; a.download = name; a.click(); URL.revokeObjectURL(url);
}

document.getElementById('export-csv')?.addEventListener('click', ()=>{
  const e = window._generatedEntries || []; if(!e.length) return alert('No hay asientos.');
  const headers = ['fecha','descripcion','moneda','debe','haber','monto'];
  const csv = [headers.join(',')].concat(e.map(r=> headers.map(h=> `"${String(r[h]||'').replace(/"/g,'""')}"`).join(','))).join('\n');
  downloadFile('asientos.csv', csv, 'text/csv');
});

document.getElementById('export-xlsx')?.addEventListener('click', ()=>{
  const e = window._generatedEntries || []; if(!e.length) return alert('No hay asientos.');
  const ws = XLSX.utils.json_to_sheet(e); const wb = XLSX.utils.book_new(); XLSX.utils.book_append_sheet(wb, ws, 'Asientos'); XLSX.writeFile(wb, 'asientos.xlsx');
});

document.getElementById('export-pdf')?.addEventListener('click', ()=>{
  const e = window._generatedEntries || []; if(!e.length) return alert('No hay asientos.');
  const { jsPDF } = window.jspdf; const doc = new jsPDF(); const rows = e.map((r,i)=>[i+1,r.fecha,r.descripcion,r.moneda,r.debe,r.haber,r.monto]);
  doc.text('Asientos generados — Finanzas IA', 10, 10); doc.autoTable({ head:[["#","Fecha","Descripcion","Moneda","Debe","Haber","Monto"]], body:rows, startY:20 });
  doc.save('asientos.pdf');
});

document.getElementById('download-original')?.addEventListener('click', ()=>{
  const f = fileInput.files[0]; if(!f) return alert('Subí el CSV primero.'); const url = URL.createObjectURL(f); const a = document.createElement('a'); a.href = url; a.download = f.name; a.click(); URL.revokeObjectURL(url);
});          fastapi==0.101.1
uvicorn[standard]==0.23.0
sqlmodel==0.0.8
sqlalchemy==2.1.4
passlib[bcrypt]==1.7.4
python-jose[cryptography]==3.3.0
pandas==2.2.2
numpy==1.26.2
scikit-learn==1.3.2
python-multipart==0.0.6
python-dotenv==1.0.0
joblib==1.3.2.  from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain,       