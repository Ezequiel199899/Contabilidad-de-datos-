  Finanzas-IA-Enterprise/
│
├── README_ENTERPRISE.md
├── .gitignore
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── backend/
    ├── main.py
    ├── auth.py
    ├── config.py
    ├── models.py
    ├── database.py
    ├── requirements.txt
    └── Dockerfile.           README_ENTERPRISE. # Finanzas IA — Enterprise Edition
Autor: Ezequiel Samuel Prilusky  
Fecha: 27 de noviembre de 2025  
Estado: **Privado** — listo para despliegue (frontend + backend)

## Resumen
Versión empresarial del prototipo “Finanzas IA”. Incluye:

- Frontend estático (HTML/CSS/JS) para carga y procesamiento básico de CSV.
- Backend en FastAPI con autenticación JWT.
- Endpoints protegidos + stub de predicción para futura IA.
- Preparado para Docker y despliegue en Render/Vercel.

## Estructura del proyecto       .gitignore.         __pycache__/
*.pyc
.env
venv/
backend/finanzas.db
.DS_Store
node_modules/
.vscode/.       __pycache__/
*.pyc
.env
venv/
backend/finanzas.db
.DS_Store
node_modules/
.vscode/.         <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>FINANZAS IA — App</title>

  <link rel="stylesheet" href="style.css">

  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.28/jspdf.plugin.autotable.min.js"></script>
</head>

<body>

<header class="site-header">
  <div class="brand">
    <h2>FINANZAS IA</h2>
    <span class="tag">Enterprise Edition</span>
  </div>
</header>

<section class="hero">
  <h1>Automatización contable con IA</h1>
  <p>Subí un CSV, mapeá columnas y generá asientos en segundos.</p>
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

<footer class="footer">
  © 2025 FINANZAS IA — Ezequiel S. Prilusky
</footer>

<script src="app.js"></script>
</body>
</html>.                               let originalData = null;

const fileInput = document.getElementById('file-input');
const previewControls = document.getElementById('preview-controls');
const tableWrap = document.getElementById('table-wrap');
const entriesWrap = document.getElementById('entries-wrap');
const entriesSection = document.getElementById('entries-section');

const selAmount = document.getElementById('col-amount');
const selDesc = document.getElementById('col-desc');
const selCurr = document.getElementById('col-curr');
const selType = document.getElementById('col-type');

fileInput?.addEventListener('change', e=>{
  const file = e.target.files[0];
  if(!file) return;

  Papa.parse(file, {
    header: true,
    skipEmptyLines: true,
    complete: res => {
      originalData = res.data;
      const headers = res.meta.fields || [];

      setupSelectors(headers);
      renderTable(originalData, headers);

      previewControls.classList.remove('hidden');
      document.getElementById('generate-row').classList.remove('hidden');
    }
  });
});

function setupSelectors(headers){
  [selAmount, selDesc, selCurr, selType].forEach(sel=>{
    sel.innerHTML = '';
    headers.forEach(h=>{
      const op = document.createElement('option');
      op.value = h;
      op.textContent = h;
      sel.appendChild(op);
    });
  });
}

function renderTable(data, headers){
  tableWrap.classList.remove('hidden');
  let html = '<table><tr>';

  headers.forEach(h => html += `<th>${h}</th>`);
  html += '</tr>';

  data.slice(0,200).forEach(row=>{
    html += '<tr>';
    headers.forEach(h => html += `<td>${row[h] || ''}</td>`);
    html += '</tr>';
  });

  html += '</table>';
  tableWrap.innerHTML = html;
}

document.getElementById('generate-entries')?.addEventListener('click', ()=>{
  if(!originalData) return alert('Subí un CSV primero.');

  const entries = [];

  originalData.forEach(r=>{
    const amount = parseFloat(r[selAmount.value]) || 0;
    if(amount === 0) return;

    const desc = r[selDesc.value];
    const curr = r[selCurr.value];
    const tipo = (r[selType.value] || '').toLowerCase();

    entries.push({
      fecha: r.date || r.fecha || '',
      descripcion: desc,
      moneda: curr,
      debe: tipo.includes('venta') ? 'Clientes' : 'Gastos',
      haber: tipo.includes('venta') ? 'Ingresos' : 'Proveedores',
      monto: Math.abs(amount)
    });
  });

  window._generatedEntries = entries;
  renderEntries(entries);
  entriesSection.classList.remove('hidden');
});

function renderEntries(entries){
  entriesWrap.innerHTML = '';

  entries.forEach((e,i)=>{
    const d = document.createElement('div');
    d.className = 'card';
    d.innerHTML = `
      <strong>#${i+1}</strong> — ${e.fecha} (${e.moneda})
      <div><em>${e.descripcion}</em></div>
      <div>DEBE: ${e.debe} — ${e.monto}</div>
      <div>HABER: ${e.haber} — ${e.monto}</div>
    `;
    entriesWrap.appendChild(d);
  });
}.                     fastapi==0.101.1
uvicorn[standard]==0.23.0
sqlmodel==0.0.8
sqlalchemy==2.1.4
passlib[bcrypt]==1.7.4
python-jose[cryptography]==3.3.0
pandas==2.2.2
numpy==1.26.2
python-multipart==0.0.6
python-dotenv==1.0.0
joblib==1.3.2.         from pydantic import BaseSettings

class Settings(BaseSettings):
    JWT_SECRET: str = "CAMBIAR"
    ALGORITHM: str = "HS256"

settings = Settings().       from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict, expires_minutes: int = 60):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.ALGORITHM)   n          from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Finanzas IA Enterprise — Backend listo"}    FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]         