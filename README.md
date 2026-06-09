# 📊 Financial Data Processing Platform

> A financial analysis app that integrates accounting data with exchange rates and commodity prices. Built with **Python (Flask)** and **Java (Spring Boot)**, it calculates trends and generates simple projections to support business decision-making.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![Java](https://img.shields.io/badge/Java-17-orange?logo=java)](https://java.com)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-brightgreen?logo=springboot)](https://spring.io)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)](https://flask.palletsprojects.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)](https://postgresql.org)
[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render)](https://contabilidad-de-datos.onrender.com/docs)

---

## 🚀 Live Demo

🔗 **API Documentation (Swagger):** [contabilidad-de-datos.onrender.com/docs](https://contabilidad-de-datos.onrender.com/docs)

---

## 📌 Features

- 📈 **Financial trend analysis** from accounting datasets
- 💱 **Exchange rate integration** for multi-currency support
- 🛢️ **Commodity price tracking**
- 🔮 **Simple financial projections** using statistical methods
- 🔗 **Microservices architecture** — Python (Flask) handles forecasting, Java (Spring Boot) manages the main API
- 📄 **REST API** fully documented with Swagger/OpenAPI

---

## 🏗️ Architecture

```
┌─────────────────────────┐        ┌──────────────────────────┐
│   Spring Boot (Java)    │──────▶│     Flask (Python)        │
│   Main API / Gateway    │  HTTP │   Forecasting Engine      │
│   Port: 8080            │        │   Port: 5000              │
└─────────────────────────┘        └──────────────────────────┘
            │
            ▼
   ┌─────────────────┐
   │   PostgreSQL     │
   │   Database       │
   └─────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Main API | Java 17, Spring Boot |
| Forecasting Service | Python 3.11, Flask, NumPy |
| Database | PostgreSQL |
| API Docs | Swagger / OpenAPI |
| Containerization | Docker |
| Deployment | Render |
| Version Control | Git / GitHub |

---

## 📡 API Endpoints

### Spring Boot — Main API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/` | Health check |
| POST | `/api/analyze` | Analyze financial data and get forecast |

### Flask — Forecasting Service

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/forecast` | Calculate average, trend and projection |

### Example Request

```json
POST /api/analyze
Content-Type: application/json

[
  { "amount": 1200.50 },
  { "amount": 1350.00 },
  { "amount": 1100.75 }
]
```

### Example Response

```json
{
  "forecast": {
    "promedio": 1217.08,
    "tendencia": -49.91,
    "proyeccion": 1050.84
  }
}
```

---

## ⚙️ Local Setup

### Prerequisites

- Java 17+
- Python 3.11+
- PostgreSQL 15+
- Docker (optional)

### 1. Clone the repository

```bash
git clone https://github.com/Ezequiel199899/Contabilidad-de-datos-.git
cd Contabilidad-de-datos-
```

### 2. Run the Flask forecasting service

```bash
cd backend-flask
pip install -r requirements.txt
python app.py
```

### 3. Run the Spring Boot API

```bash
cd backend-spring
./mvnw spring-boot:run
```

### 4. Run with Docker (recommended)

```bash
docker-compose up --build
```

---

## 📂 Project Structure

```
Contabilidad-de-datos-/
├── backend-flask/          # Python forecasting microservice
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── backend-spring/         # Java main API
│   ├── src/
│   ├── pom.xml
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 👤 Author

**Ezequiel Samuel Prilusky**
Junior Backend Developer | Python · Java · FastAPI · PostgreSQL

🌐 [Portfolio](https://ezequiel199899.github.io) · 🐙 [GitHub](https://github.com/Ezequiel199899) · 📧 priluskyezequielsamuel@gmail.com · 📍 Mendoza, Argentina · 🛫 Open to Remote

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Ezequiel Prilusky — Junior Backend Developer | Python · Java · FastAPI · Flask</title>
  <meta name="description" content="Junior Backend Developer especializado en Python, Java, FastAPI, Flask, Spring Boot y PostgreSQL. Disponible para trabajo remoto en Argentina, LATAM y España."/>
  <meta name="keywords" content="backend developer, python developer, java developer, fastapi, flask, spring boot, postgresql, microservices, REST API, remoto, Argentina, Mendoza, junior developer"/>
  <meta name="author" content="Ezequiel Samuel Prilusky"/>
  <meta name="robots" content="index, follow"/>
  <link rel="canonical" href="https://ezequiel199899.github.io"/>

  <!-- Open Graph (LinkedIn, WhatsApp, Facebook) -->
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://ezequiel199899.github.io"/>
  <meta property="og:title" content="Ezequiel Prilusky — Junior Backend Developer"/>
  <meta property="og:description" content="Backend Developer especializado en Python, Java, FastAPI y microservicios. Proyecto en producción. Disponible para trabajo remoto."/>
  <meta property="og:locale" content="es_AR"/>

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary"/>
  <meta name="twitter:title" content="Ezequiel Prilusky — Junior Backend Developer"/>
  <meta name="twitter:description" content="Backend Developer especializado en Python, Java, FastAPI y microservicios. Disponible para trabajo remoto."/>

  <!-- Schema.org para Google -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Ezequiel Samuel Prilusky",
    "jobTitle": "Junior Backend Developer",
    "url": "https://ezequiel199899.github.io",
    "email": "priluskyezequielsamuel@gmail.com",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Mendoza",
      "addressCountry": "AR"
    },
    "sameAs": ["https://github.com/Ezequiel199899"],
    "knowsAbout": ["Python", "Java", "FastAPI", "Flask", "Spring Boot", "PostgreSQL", "REST APIs", "Docker", "Microservices"]
  }
  </script>

  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:        #0D1117;
      --bg2:       #161B22;
      --bg3:       #1C2333;
      --green:     #00FF9C;
      --green-dim: #00cc7a;
      --blue:      #58A6FF;
      --text:      #E6EDF3;
      --muted:     #8B949E;
      --border:    #30363D;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      line-height: 1.7;
    }

    /* ── NAV ── */
    nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; justify-content: space-between; align-items: center;
      padding: 1rem 2.5rem;
      background: rgba(13,17,23,0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
    }
    .nav-logo {
      font-family: 'JetBrains Mono', monospace;
      color: var(--green);
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: 0.05em;
    }
    .nav-links { display: flex; gap: 2rem; list-style: none; }
    .nav-links a {
      color: var(--muted);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--green); }

    /* ── HERO ── */
    #hero {
      min-height: 100vh;
      display: flex; flex-direction: column; justify-content: center; align-items: center;
      text-align: center;
      padding: 7rem 2rem 4rem;
      position: relative;
      overflow: hidden;
    }
    #hero::before {
      content: '';
      position: absolute; inset: 0;
      background: radial-gradient(ellipse at 50% 40%, rgba(0,255,156,0.07) 0%, transparent 65%);
      pointer-events: none;
    }
    .hero-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: var(--green);
      letter-spacing: 0.15em;
      text-transform: uppercase;
      margin-bottom: 1.2rem;
    }
    .hero-photo {
      width: 120px; height: 120px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid var(--green);
      margin-bottom: 1.8rem;
      box-shadow: 0 0 30px rgba(0,255,156,0.2);
    }
    .hero-name {
      font-family: 'JetBrains Mono', monospace;
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 700;
      color: var(--text);
      line-height: 1.1;
      margin-bottom: 1rem;
    }
    .hero-name span { color: var(--green); }
    .typing-line {
      font-family: 'JetBrains Mono', monospace;
      font-size: clamp(0.9rem, 2vw, 1.1rem);
      color: var(--blue);
      min-height: 1.6em;
      margin-bottom: 1.5rem;
    }
    .cursor {
      display: inline-block;
      width: 2px; height: 1.1em;
      background: var(--green);
      vertical-align: middle;
      animation: blink 0.8s step-end infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }

    .hero-desc {
      max-width: 540px;
      color: var(--muted);
      font-size: 1rem;
      margin-bottom: 2.5rem;
      line-height: 1.8;
    }
    .hero-cta {
      display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;
    }
    .btn {
      display: inline-block;
      padding: 0.75rem 1.75rem;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
      cursor: pointer;
    }
    .btn-primary {
      background: var(--green);
      color: #0D1117;
      border: 2px solid var(--green);
    }
    .btn-primary:hover { background: var(--green-dim); border-color: var(--green-dim); }
    .btn-outline {
      background: transparent;
      color: var(--green);
      border: 2px solid var(--green);
    }
    .btn-outline:hover { background: rgba(0,255,156,0.08); }

    .scroll-hint {
      position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%);
      color: var(--muted); font-size: 0.75rem; letter-spacing: 0.1em;
      display: flex; flex-direction: column; align-items: center; gap: 0.4rem;
    }
    .scroll-arrow { animation: bounce 1.8s infinite; }
    @keyframes bounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(6px)} }

    /* ── SECTIONS ── */
    section { padding: 5rem 2rem; }
    .container { max-width: 900px; margin: 0 auto; }
    .section-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      color: var(--green);
      letter-spacing: 0.2em;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }
    .section-title {
      font-size: clamp(1.6rem, 3vw, 2.2rem);
      font-weight: 600;
      color: var(--text);
      margin-bottom: 1rem;
    }
    .section-sub {
      color: var(--muted);
      max-width: 580px;
      margin-bottom: 3rem;
      font-size: 0.95rem;
    }
    .divider {
      width: 40px; height: 3px;
      background: var(--green);
      border-radius: 2px;
      margin-bottom: 3rem;
    }

    /* ── SERVICES ── */
    #services { background: var(--bg2); }
    .services-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1.5rem;
    }
    .service-card {
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.75rem;
      transition: border-color 0.2s, transform 0.2s;
    }
    .service-card:hover {
      border-color: var(--green);
      transform: translateY(-4px);
    }
    .service-icon {
      font-size: 1.8rem;
      margin-bottom: 1rem;
    }
    .service-title {
      font-weight: 600;
      font-size: 1rem;
      color: var(--text);
      margin-bottom: 0.6rem;
    }
    .service-desc {
      color: var(--muted);
      font-size: 0.875rem;
      line-height: 1.7;
    }
    .service-tags {
      display: flex; flex-wrap: wrap; gap: 0.4rem;
      margin-top: 1rem;
    }
    .tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      background: rgba(0,255,156,0.08);
      color: var(--green);
      border: 1px solid rgba(0,255,156,0.2);
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
    }

    /* ── SKILLS ── */
    #skills { background: var(--bg); }
    .skills-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.2rem;
    }
    .skill-group {
      background: var(--bg2);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.25rem 1.5rem;
    }
    .skill-group-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: var(--green);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 0.75rem;
    }
    .skill-list {
      list-style: none;
      display: flex; flex-wrap: wrap; gap: 0.4rem;
    }
    .skill-list li {
      font-size: 0.825rem;
      color: var(--text);
      background: var(--bg3);
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      border: 1px solid var(--border);
    }

    /* ── PROJECT ── */
    #project { background: var(--bg2); }
    .project-card {
      background: var(--bg3);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 2.5rem;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3rem;
      align-items: start;
    }
    .project-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: var(--green);
      letter-spacing: 0.15em;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }
    .project-title {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 1rem;
    }
    .project-desc {
      color: var(--muted);
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
      line-height: 1.8;
    }
    .project-links { display: flex; gap: 0.75rem; flex-wrap: wrap; }
    .arch-box {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      color: var(--muted);
      line-height: 1.9;
    }
    .arch-box .hl { color: var(--green); }
    .arch-box .hl2 { color: var(--blue); }
    .feature-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem; }
    .feature-list li { font-size: 0.875rem; color: var(--muted); display: flex; gap: 0.5rem; align-items: flex-start; }
    .feature-list li::before { content: '→'; color: var(--green); flex-shrink: 0; margin-top: 0.05rem; }

    /* ── CONTACT ── */
    #contact { background: var(--bg); }
    .contact-card {
      background: var(--bg2);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 3rem;
      text-align: center;
      max-width: 600px;
      margin: 0 auto;
    }
    .contact-card h3 {
      font-size: 1.5rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
    }
    .contact-card p {
      color: var(--muted);
      font-size: 0.9rem;
      margin-bottom: 2rem;
    }
    .contact-links {
      display: flex; flex-direction: column; gap: 0.75rem; align-items: center;
    }
    .contact-link {
      display: flex; align-items: center; gap: 0.75rem;
      color: var(--text);
      text-decoration: none;
      font-size: 0.9rem;
      padding: 0.75rem 1.5rem;
      border: 1px solid var(--border);
      border-radius: 8px;
      width: 100%; max-width: 340px;
      transition: all 0.2s;
    }
    .contact-link:hover { border-color: var(--green); color: var(--green); }
    .contact-link span { font-size: 1.1rem; }

    /* ── FOOTER ── */
    footer {
      text-align: center;
      padding: 2rem;
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: 0.8rem;
      font-family: 'JetBrains Mono', monospace;
    }

    @media (max-width: 680px) {
      nav { padding: 1rem 1.25rem; }
      .nav-links { gap: 1rem; }
      .project-card { grid-template-columns: 1fr; gap: 1.5rem; }
      .contact-card { padding: 2rem 1.25rem; }
    }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-logo">ezequiel.dev</div>
  <ul class="nav-links">
    <li><a href="#services">Servicios</a></li>
    <li><a href="#skills">Stack</a></li>
    <li><a href="#project">Proyecto</a></li>
    <li><a href="#contact">Contacto</a></li>
  </ul>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-tag">// disponible para trabajar remotamente</div>
  <img
    class="hero-photo"
    src="https://avatars.githubusercontent.com/u/Ezequiel199899"
    onerror="this.src='https://ui-avatars.com/api/?name=Ezequiel+Prilusky&background=00FF9C&color=0D1117&size=200&bold=true'"
    alt="Ezequiel Prilusky"
  />
  <h1 class="hero-name">Ezequiel <span>Prilusky</span></h1>
  <div class="typing-line" id="typing-line"><span class="cursor"></span></div>
  <p class="hero-desc">
    Junior Backend Developer especializado en APIs, microservicios y análisis de datos.
    Construyo soluciones backend reales, deployadas en producción y listas para escalar.
  </p>
  <div class="hero-cta">
    <a href="#contact" class="btn btn-primary">Contratame</a>
    <a href="https://contabilidad-de-datos.onrender.com/docs" target="_blank" class="btn btn-outline">Ver API en vivo →</a>
  </div>
  <div class="scroll-hint">
    <span>scroll</span>
    <span class="scroll-arrow">↓</span>
  </div>
</section>

<!-- SERVICES -->
<section id="services">
  <div class="container">
    <div class="section-label">// lo que ofrezco</div>
    <h2 class="section-title">Mis Servicios</h2>
    <div class="divider"></div>
    <div class="services-grid">

      <div class="service-card">
        <div class="service-icon">⚙️</div>
        <div class="service-title">Desarrollo de APIs REST</div>
        <div class="service-desc">Diseño, construyo y documento APIs robustas con autenticación, validación y manejo de errores. Documentación Swagger/OpenAPI incluida.</div>
        <div class="service-tags">
          <span class="tag">FastAPI</span>
          <span class="tag">Flask</span>
          <span class="tag">Swagger</span>
        </div>
      </div>

      <div class="service-card">
        <div class="service-icon">🏗️</div>
        <div class="service-title">Arquitectura de Microservicios</div>
        <div class="service-desc">Diseño sistemas con servicios independientes que se comunican entre sí. Experiencia con Python y Java trabajando en conjunto.</div>
        <div class="service-tags">
          <span class="tag">Python</span>
          <span class="tag">Java</span>
          <span class="tag">Spring Boot</span>
        </div>
      </div>

      <div class="service-card">
        <div class="service-icon">🗄️</div>
        <div class="service-title">Bases de Datos & Backend</div>
        <div class="service-desc">Modelado, optimización y gestión de bases de datos relacionales. Integración de múltiples fuentes de datos en un solo sistema.</div>
        <div class="service-tags">
          <span class="tag">PostgreSQL</span>
          <span class="tag">SQL</span>
          <span class="tag">JSON</span>
        </div>
      </div>

      <div class="service-card">
        <div class="service-icon">📊</div>
        <div class="service-title">Análisis de Datos & Automatización</div>
        <div class="service-desc">Procesamiento de datasets financieros, generación de reportes automatizados y proyecciones con Python.</div>
        <div class="service-tags">
          <span class="tag">Pandas</span>
          <span class="tag">NumPy</span>
          <span class="tag">Data Analysis</span>
        </div>
      </div>

      <div class="service-card">
        <div class="service-icon">☁️</div>
        <div class="service-title">Deploy & DevOps básico</div>
        <div class="service-desc">Containerización con Docker y deploy en la nube. Mantenimiento del proyecto con Git/GitHub y historial de commits estructurado.</div>
        <div class="service-tags">
          <span class="tag">Docker</span>
          <span class="tag">Render</span>
          <span class="tag">GitHub</span>
        </div>
      </div>

      <div class="service-card">
        <div class="service-icon">🤖</div>
        <div class="service-title">Integración de IA & ML básico</div>
        <div class="service-desc">Integración de modelos de machine learning en aplicaciones backend. Formación en Data Science e IA aplicada.</div>
        <div class="service-tags">
          <span class="tag">ML</span>
          <span class="tag">Data Science</span>
          <span class="tag">Oracle ONE</span>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- SKILLS -->
<section id="skills">
  <div class="container">
    <div class="section-label">// tecnologías</div>
    <h2 class="section-title">Stack Técnico</h2>
    <div class="divider"></div>
    <div class="skills-grid">
      <div class="skill-group">
        <div class="skill-group-title">Lenguajes</div>
        <ul class="skill-list">
          <li>Python</li>
          <li>Java</li>
          <li>SQL</li>
        </ul>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Frameworks</div>
        <ul class="skill-list">
          <li>FastAPI</li>
          <li>Flask</li>
          <li>Spring Boot</li>
        </ul>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Bases de datos</div>
        <ul class="skill-list">
          <li>PostgreSQL</li>
          <li>MySQL</li>
          <li>JSON</li>
        </ul>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Herramientas</div>
        <ul class="skill-list">
          <li>Git</li>
          <li>GitHub</li>
          <li>Docker</li>
          <li>Swagger</li>
        </ul>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Data & IA</div>
        <ul class="skill-list">
          <li>Pandas</li>
          <li>NumPy</li>
          <li>ML básico</li>
        </ul>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Cloud & Deploy</div>
        <ul class="skill-list">
          <li>Render</li>
          <li>Docker</li>
          <li>REST APIs</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- PROJECT -->
<section id="project">
  <div class="container">
    <div class="section-label">// proyecto en producción</div>
    <h2 class="section-title">Financial Data Platform</h2>
    <div class="divider"></div>
    <div class="project-card">
      <div>
        <div class="project-label">Proyecto personal · Live en producción</div>
        <div class="project-title">Plataforma de Análisis Financiero</div>
        <p class="project-desc">
          Sistema completo de procesamiento y análisis de datos financieros con arquitectura de microservicios. Integra tipos de cambio, precios de materias primas y genera proyecciones estadísticas automáticas.
        </p>
        <ul class="feature-list">
          <li>Dos microservicios independientes comunicados por HTTP</li>
          <li>APIs REST documentadas con Swagger/OpenAPI</li>
          <li>Integración de datos financieros en tiempo real</li>
          <li>Motor de proyecciones estadísticas con NumPy</li>
          <li>Containerizado con Docker, deployado en Render</li>
        </ul>
        <div class="project-links">
          <a href="https://contabilidad-de-datos.onrender.com/docs" target="_blank" class="btn btn-primary">API en vivo →</a>
          <a href="https://github.com/Ezequiel199899/Contabilidad-de-datos-" target="_bla