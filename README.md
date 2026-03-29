
# 💰 Finanzas AI

Aplicación full stack que permite a pequeñas empresas analizar su flujo de caja, detectar anomalías en gastos y generar insights automáticos usando análisis de datos e inteligencia artificial.

---

## 🎯 Problema

Muchas pequeñas empresas no cuentan con herramientas claras para entender sus ingresos y gastos, lo que dificulta detectar problemas financieros a tiempo y tomar decisiones informadas.

---

## 💡 Solución

Finanzas AI procesa datos financieros, identifica patrones de comportamiento, detecta anomalías y genera resúmenes automáticos que ayudan a mejorar la toma de decisiones.

---

## 🚀 Funcionalidades

- Registro y autenticación de usuarios (JWT)
- Gestión de empresas
- Análisis de ingresos y gastos
- Detección de anomalías en transacciones
- Generación de insights automáticos con IA
- Endpoint de predicción (`/predict-summary`)

---

## ⚙️ Tecnologías

- **Backend:** FastAPI
- **Base de datos:** SQLite + SQLModel
- **Autenticación:** JWT (python-jose)
- **Procesamiento de datos:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Otros:** Uvicorn, Passlib

---

## 🧠 Arquitectura

El proyecto está organizado en módulos:

- `app/` → API principal (FastAPI)
- `models/` → Modelos de base de datos
- `api/` → Endpoints (auth, usuarios, predicción)
- `utils/` → Procesamiento de datos
- `data/` → Datos de prueba

---

## ▶️ Cómo ejecutar el proyecto

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn app.main:app --reload --port 8000.          POST /auth/register.          POST /auth/token.       backend/
 ├── app/
 │   ├── main.py
 │   ├── api.py
 │   ├── api_predict.py
 │   ├── db.py
 │   ├── models.py
 │   ├── auth.py
 │   └── predictor.py
 ├── requirements.txt
 └── README.md.       from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    users: List["User"] = Relationship(back_populates="company")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    hashed_password: str
    is_active: bool = True
    role: str = "user"

    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="users").       t.        from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from .db import get_session
from .models import User

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=8)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user.          from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlmodel import select
from .db import get_session
from .models import User, Company
from .auth import hash_password, verify_password, create_access_token

router = APIRouter()

class RegisterPayload(BaseModel):
    email: str
    password: str
    full_name: str = ""
    company_name: str = ""

class LoginPayload(BaseModel):
    email: str
    password: str

@router.post("/auth/register")
def register(payload: RegisterPayload):
    with next(get_session()) as session:

        comp = None
        if payload.company_name:
            stmt = select(Company).where(Company.name == payload.company_name)
            comp = session.exec(stmt).first()

            if not comp:
                comp = Company(name=payload.company_name)
                session.add(comp)
                session.commit()
                session.refresh(comp)

        stmt = select(User).where(User.email == payload.email)
        if session.exec(stmt).first():
            raise HTTPException(status_code=400, detail="Email ya registrado")

        user = User(
            email=payload.email,
            full_name=payload.full_name,
            hashed_password=hash_password(payload.password),
            company_id=comp.id if comp else None
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token}.        from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .auth import get_current_user
from .predictor import predict_summary

router = APIRouter()

class RowsPayload(BaseModel):
    rows: list

@router.post("/predict-summary")
def predict_summary_endpoint(payload: RowsPayload, user = Depends(get_current_user)):
    result = predict_summary(payload.rows)
    return {"summaryText": result}.      def predict_summary(rows):
    total = sum(r.get("amount", 0) for r in rows)

    if total < 0:
        return "Pérdidas detectadas. Revisar gastos."
    elif total > 0:
        return "Balance positivo. Buen desempeño."
    else:
        return "Balance neutro.".     from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router
from .api_predict import router as predict_router
from .db import create_db_and_tables

app = FastAPI(title="Finanzas AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(predict_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status": "ok"}.       fastapi
uvicorn
sqlmodel
passlib[bcrypt]
python-jose
pydantic.               