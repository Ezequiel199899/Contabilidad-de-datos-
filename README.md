from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import User, Company
from app.auth import authenticate, hash_password
from app.predictor import predict_income

router = APIRouter()

# ---------------- USERS ----------------

@router.post("/register")
def register(user: User, session: Session = Depends(get_session)):
    user.password = hash_password(user.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.post("/login")
def login(data: User, session: Session = Depends(get_session)):
    user = authenticate(data.email, data.password, session)
    return {"message": "Login successful", "user_id": user.id}

# ---------------- COMPANIES ----------------

@router.post("/companies")
def create_company(company: Company, session: Session = Depends(get_session)):
    session.add(company)
    session.commit()
    session.refresh(company)
    return company

@router.get("/companies")
def get_companies(session: Session = Depends(get_session)):
    return session.exec(select(Company)).all()

@router.put("/companies/{company_id}")
def update_company(company_id: int, updated: Company, session: Session = Depends(get_session)):
    company = session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    company.name = updated.name
    company.revenue = updated.revenue
    session.commit()
    return company

@router.delete("/companies/{company_id}")
def delete_company(company_id: int, session: Session = Depends(get_session)):
    company = session.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    session.delete(company)
    session.commit()
    return {"message": "Deleted"}

# ---------------- AI ----------------  # 💼 Contabilidad de Datos API

API backend desarrollada con FastAPI para la gestión de empresas, autenticación de usuarios y predicción de ingresos.

## 🚀 Tecnologías

- FastAPI
- SQLModel (SQLite)
- Python
- Passlib (seguridad)

## 🧠 Funcionalidades

- Registro y login de usuarios con hashing de contraseñas
- CRUD completo de empresas
- Predicción de ingresos (simulación basada en tendencias)
- API REST documentada automáticamente con Swagger

## 📊 Caso de uso

Esta aplicación permite a pequeñas empresas:

- Gestionar sus datos financieros
- Centralizar información
- Obtener estimaciones rápidas de ingresos futuros

## 🔥 Demo

Acceder a la documentación interactiva:

http://localhost:8000/docs

## ⚙️ Instalación

```bash
pip install -r requirements.txt.  uvicorn app.main:app --reload.                            

@router.get("/predict")
def predict():
    return {"predicted_income": predict_income()}.        ---

# 🚀 🔥 3. DETALLE PRO (MUY IMPORTANTE)

👉 En tu repo agregá esto:

## 📁 `.gitignore`

```txt
__pycache__/
*.pyc
database.db.      @router.get("/health")
def health():
    return {"status": "ok"}.                