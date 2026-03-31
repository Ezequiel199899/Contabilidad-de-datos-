COMMIT.   app/main.py.  from fastapi import FastAPI
from app.api import router as api_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()

app.include_router(api_router, prefix="/api").  COMMIT.  app/api.py.    from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db import get_session
from app.models import User, Company
from app.auth import authenticate, hash_password
from app.predictor import predict_income

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

@router.get("/predict")
def predict():
    return {"predicted_income": predict_income()}

@router.get("/health")
def health():
    return {"status": "ok"}.  COMMIT.  app/db.py.   from sqlmodel import SQLModel, create_engine, Session

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session. COMMIT. app/models.py.    from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    revenue: float.     COMMITv.    app/auth.py.   from fastapi import  revenue: floatT TPException
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

    return user.   COMMIT.    app/predictor.py. import random

def predict_income():
    base = random.randint(800, 1500)
    trend = random.uniform(0.9, 1.2)
    return round(base * trend, 2).    COMMIT.   requirements.txt.  fastapi
uvicorn
sqlmodel
passlib[bcrypt].   COMMIT.     