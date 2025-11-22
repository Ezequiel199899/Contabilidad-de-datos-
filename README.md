        # models.py
from typing import Optional
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
    role: str = "user"  # admin/user
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
    company: Optional[Company] = Relationship(back_populates="users")   # db.py
from sqlmodel import create_engine, SQLModel, Session
from pathlib import Path

DB_FILE = Path(__file__).resolve().parents[1] / "finanzas.db"
DATABASE_URL = f"sqlite:///{DB_FILE}".                  

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session.               vbvv.  # api.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from .db import get_session
from sqlmodel import Session, select
from .models import User, Company
from .auth import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter()

class RegisterPayload(BaseModel):
    email: str
    password: str
    full_name: str = ""
    company_name: str = ""

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/auth/register", response_model=TokenResponse)
def register(payload: RegisterPayload):
    with next(get_session()) as session:
        # create or get company
        comp = None
        if payload.company_name:
            stmt = select(Company).where(Company.name == payload.company_name)
            comp = session.exec(stmt).first()
            if not comp:
                comp = Company(name=payload.company_name)
                session.add(comp)
                session.commit()
                session.refresh(comp)
        # check user
        stmt = select(User).where(User.email == payload.email)
        if session.exec(stmt).first():
            raise HTTPException(status_code=400, detail="Email ya registrado")
        hashed = hash_password(payload.password)
        user = User(email=payload.email, full_name=payload.full_name, hashed_password=hashed, company_id=(comp.id if comp else None))
        session.add(user)
        session.commit()
        session.refresh(user)
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token}

class LoginPayload(BaseModel):
    email: str
    password: str

@router.post("/auth/token", response_model=TokenResponse)
def login(payload: LoginPayload):
    with next(get_session()) as session:
        stmt = select(User).where(User.email == payload.email)
        user = session.exec(stmt).first()
        if not user or not verify_password(payload.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token}

# protected example: list companies of user
@router.get("/me/companies")
def my_companies(current_user: User = Depends(get_current_user)):
    return {"company_id": current_user.company_id, "role": current_user.role, "email": current_user.email}.               # main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router as api_router
from .db import create_db_and_tables

app = FastAPI(title="Finanzas AI API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(api_router, prefix="")

# crear BD al iniciar
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"status":"ok"}.   // auth helpers (frontend)
function saveToken(t){ localStorage.setItem('fa_token', t); }
function getToken(){ return localStorage.getItem('fa_token'); }
function authHeaders(){ const tk = getToken(); return tk ? {'Authorization':'Bearer '+tk} : {}; }

// register
async function registerUser(email, pass, name, company){
  const res = await fetch('/auth/register', {
    method:'POST', headers:{'Content-Type':'application/json'}, 
    body:JSON.stringify({email, password:pass, full_name:name, company_name:company})
  });
  if(!res.ok) throw await res.text();
  const j = await res.json(); saveToken(j.access_token);
  alert('Registrado y logueado');
}

// login
async function loginUser(email, pass){
  const res = await fetch('/auth/token', {
    method:'POST', headers:{'Content-Type':'application/json'}, 
    body:JSON.stringify({email, password:pass})
  });
  if(!res.ok) throw await res.text();
  const j = await res.json(); saveToken(j.access_token); alert('Logueado');
}

// use token when calling predict-summary
document.getElementById('run-ai').addEventListener('click', async ()=>{
  if(!originalData) return alert('Subí un CSV primero.');
  const token = getToken();
  if(!token) return alert('Logueate primero.');
  try {
    const res = await fetch('/predict-summary', { method:'POST', headers: {...authHeaders(), 'Content-Type':'application/json'}, body: JSON.stringify({rows: originalData.slice(0,200)}) });
    const j = await res.json();
    document.getElementById('ai-output').textContent = j.summaryText;
  } catch(e){ console.error(e); alert('Error comunicando con backend'); }
});                      # api_predict.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .auth import get_current_user
from .predictor import predict_summary

router = APIRouter()

class RowsPayload(BaseModel):
    rows: list

@router.post('/predict-summary')
def predict_summary_endpoint(payload: RowsPayload, current_user = Depends(get_current_user)):
    # aquí podemos personalizar según current_user.company_id
    out = predict_summary(payload.rows)
    return {"summaryText": out}.           fastapi
uvicorn[standard]
sqlmodel
sqlalchemy
passlib[bcrypt]
python-jose[cryptography]
pandas
scikit-learn
joblib
python-multipart
pydantic
numpy.           # Finanzas AI — RUN & TEST

## Backend (local)
1. Crear virtualenv
2. pip install -r backend/requirements.txt
3. cd backend
4. uvicorn app.main:app --reload --port 8000

Al arrancar crea `finanzas.db` con tablas User/Company.

## Frontend
Abrir `frontend/index.html` (o servirlo con GitHub Pages). Para usar endpoints protegidos debes:
- Registrarte con POST /auth/register o usar /auth/token
- Guardar token en localStorage (el frontend ya lo hace)
- Llamar al botón "Analizar con IA" después de loguearte

## Credenciales de prueba
Registrar un usuario en UI o usar:
- email: demo@finanzas.ai
- password: Demo1234!