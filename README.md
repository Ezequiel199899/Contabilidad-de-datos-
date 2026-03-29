from fastapi import FastAPI
from app.api import router as api_router
from app.api_predict import router as predict_router

app = FastAPI(title="Contabilidad API")

app.include_router(api_router, prefix="/api")
app.include_router(predict_router, prefix="/predict").        from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session.         from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str.          from fastapi import HTTPException
from sqlmodel import Session, select
from app.models import User

def authenticate(email: str, password: str, session: Session):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user.         t.       from fastapi import APIRouter
from app.predictor import predict_income

router = APIRouter()

@router.get("/")
def predict():
    return {"prediction": predict_income()}.        def predict_income():
    return 1000.          fastapi
uvicorn
sqlmodel.                              