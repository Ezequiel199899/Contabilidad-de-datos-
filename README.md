from fastapi import APIRouter, Depends, HTTPException
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
    return {"status": "ok"}.      #!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port 10000.      fastapi
uvicorn
sqlmodel
passlib[bcrypt].  bl           