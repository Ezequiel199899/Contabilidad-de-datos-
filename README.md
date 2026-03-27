mkdir finanzas_ai
cd finanzas_ai
mkdir app
mkdir app/utils
mkdir frontend.   pip install fastapi uvicorn sqlmodel sqlalchemy passlib[bcrypt] python-jose pandas scikit-learn.      from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    users: list["User"] = Relationship(back_populates="company")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    hashed_password: str
    is_active: bool = True
    role: str = "user"
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="users").      from sqlmodel import create_engine, SQLModel, Session
from pathlib import Path

DB_FILE = Path(__file__).resolve().parents[1] / "finanzas.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session.              from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "123456789"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return bcrypt.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.verify(password, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user():
    return {"id": 1}  # simplificado para pruebas.            from fastapi import APIRouter, HTTPException
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
            company_id=(comp.id if comp else None)
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token}.           from fastapi import APIRouter

router = APIRouter()

@router.post("/predict-summary")
def predict_summary():
    return {"summaryText": "Resumen generado por IA 🚀"}.   v.      from fastapi import APIRouter

router = APIRouter()

@router.post("/predict-summary")
def predict_summary():
    return {"summaryText": "Resumen generado por IA 🚀"}.    from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router
from .api_predict import router as predict_router
from .db import create_db_and_tables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router)
app.include_router(predict_router)

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status": "ok"}.            <!DOCTYPE html>
<html>
<body>

<h1>Finanzas AI</h1>

<input id="email" placeholder="email"><br>
<input id="pass" placeholder="password"><br>
<button onclick="register()">Registrarse</button>

<button id="run-ai">Analizar</button>

<pre id="out"></pre>

<script src="script.js"></script>

</body>
</html>.      async function register(){
    const email = document.getElementById('email').value;
    const pass = document.getElementById('pass').value;

    const res = await fetch('http://localhost:8000/auth/register',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({email, password:pass})
    });

    const j = await res.json();
    localStorage.setItem("token", j.access_token);
    alert("Registrado");
}

document.getElementById('run-ai').onclick = async ()=>{
    const res = await fetch('http://localhost:8000/predict-summary',{
        method:'POST'
    });

    const j = await res.json();
    document.getElementById('out').textContent = j.summaryText;
};       uvicorn app.main:app --reload.        frontend/index.html       