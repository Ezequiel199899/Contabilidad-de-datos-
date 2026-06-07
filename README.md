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

🔗 [GitHub](https://github.com/Ezequiel199899) · 📍 Argentina · 🌐 Open to Remote Opportunities

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
   