ir contabilidad-api
cd contabilidad-api
mkdir app
from fastapi import FastAPI
from app.api import router as api_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()

app.include_router(api_router, prefix="/api")from fastapi import FastAPI
from app.api import router as api_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()

app.include_router(api_router, prefix="/api") from fastapi import HTTPException
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

    return userfrom fastapi import HTTPException
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
        raise HTTPException(status_code=401, detail="Invalid credentials")  from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session     from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    revenue: float    import random

def predict_income():
    base = random.randint(800, 1500)
    trend = random.uniform(0.9, 1.2)
    return round(base * trend, 2)    fastapi
uvicorn
sqlmodel
passlib[bcrypt]

    return user   #!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port 10000  __pycache__/
*.pyc
database.db __pycache__/
*.pyc
database.db  services:
  - type: web
    name: contabilidad-api
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn app.main:app --host 0.0.0.0 --port 10000"
    plan: free  git init
git add .
git commit -m "API lista"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/contabilidad-api.git
git push -u origin main
