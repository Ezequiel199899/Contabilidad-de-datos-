finanzas-ai/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api.py
│   │   ├── api_predict.py
│   │   ├── auth.py
│   │   ├── db.py
│   │   ├── models.py
│   │   └── predictor.py
│   │
│   ├── requirements.txt
│
├── frontend/
│   └── index.html
│
├── README.md
├── .gitignore.           from typing import Optional, List
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
    company: Optional[Company] = Relationship(back_populates="users").            from typing import Optional, List
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
    company: Optional[Company] = Relationship(back_populates="users").             from typing import Optional, List
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
    company: Optional[Company] = Relationship(back_populates="users").              from sqlmodel import create_engine, SQLModel, Session
from pathlib import Path

DB_FILE = Path(__file__).resolve().parents[1] / "finanzas.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session.            from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .db import get_session
from .models import User

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    with next(get_session()) as session:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user.          from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import select

from .db import get_session
from .models import User, Company
from .auth import hash_password, verify_password, create_access_token, get_current_user

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
        return {"access_token": token}


@router.post("/auth/token")
def login(payload: LoginPayload):
    with next(get_session()) as session:
        stmt = select(User).where(User.email == payload.email)
        user = session.exec(stmt).first()

        if not user or not verify_password(payload.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token}


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "role": current_user.role,
        "company_id": current_user.company_id
    }.         from fastapi import APIRouter, Depends
from pydantic import BaseModel

from .auth import get_current_user
from .predictor import predict_summary

router = APIRouter()


class RowsPayload(BaseModel):
    rows: list


@router.post("/predict-summary")
def predict_summary_endpoint(payload: RowsPayload, current_user=Depends(get_current_user)):
    result = predict_summary(payload.rows)
    return {"summaryText": result}.         def predict_summary(rows):
    return "Análisis generado por IA (demo)".            from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router as api_router
from .api_predict import router as predict_router
from .db import create_db_and_tables

app = FastAPI(title="Finanzas AI API")

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
    return {"status": "ok"}.     v.           fastapi
uvicorn
sqlmodel
passlib[bcrypt]
python-jose
pydantic.         __pycache__/
*.db
.env.          
 