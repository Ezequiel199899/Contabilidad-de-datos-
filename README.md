from fastapi import FastAPI
from app.api import router as api_router
from app.api_predict import router as predict_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()

app.include_router(api_router, prefix="/api")
app.include_router(predict_router, prefix="/predict").         from fastapi import HTTPException
from sqlmodel import Session, select
from passlib.context import CryptContext
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def authenticate(email: str, password: str, session: Session):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user       from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models import User, Company
from app.auth import authenticate, hash_password

router = APIRouter()

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

@router.get("/companies")
def get_companies(session: Session = Depends(get_session)):
    return session.exec(select(Company)).all().           fastapi
uvicorn
sqlmodel
passlib[bcrypt].       # Contabilidad de Datos API

Aplicación Full Stack con foco en backend y análisis de datos, desarrollada con FastAPI para la gestión de empresas, procesamiento de datos financieros y predicción de ingresos.

---

## Funcionalidades

- Registro y login de usuarios (con hashing de contraseña)
- Gestión de empresas
- Predicción de ingresos
- API REST documentada automáticamente

---

## Demo

Una vez ejecutado el proyecto, acceder a:

http://localhost:8000/docs

Swagger UI interactivo para probar la API.

---

## Instalación

```bash
pip install -r requirements.txt.     uvicorn app.main:app --reload.                               