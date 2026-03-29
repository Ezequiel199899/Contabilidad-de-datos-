    
app/auth.py.           from fastapi import FastAPI
from app.api import router as api_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()

app.include_router(api_router, prefix="/api").         from fastapi import APIRouter, Depends
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
    return session.exec(select(Company)).all().   app/auth.py.      from fastapi import HTTPException
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
    return user.   app/db.py.       from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield sessionapp/models.py.       from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
  revenue: float.  from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    revenue: float.          app/predictor.py    import random

def predict_income():
    base = random.randint(800, 1500)
    trend = random.uniform(0.9, 1.2)
    return round(base * trend, .  import random

def predict_income():
    base = random.randint(800, 1500)
    trend = random.uniform(0.9, 1.2)
    return round(base * trend, 2)      requirements.txt.     fastapi
uvicorn
sqlmodel
passlib[bcrypt].     README.md.    # Contabilidad de Datos API

Aplicación Full Stack con foco en backend y análisis de datos.

## Funcionalidades

- Registro y login de usuarios
- Gestión de empresas
- Predicción de ingresos

## Demo

http://localhost:8000/docs

## Instalación

pip install -r requirements.txt

## Ejecutar

uvicorn app.main:app --reload.  
                                       