ofrom fastapi import FastAPI
from app.api import router as api_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()

app.include_router(api_router, prefix="/api")        i import FastAPI
from app.api import router as api_router
from app.db import create_db

app = FastAPI(title="Contabilidad API")

create_db()
          
app.include_router(api_router, prefix="/api")   from sqlmodel import SQLModel, create_engine, Session

sqlite_url = "sqlite:///database.db"   
engine = create_engine(sqlite_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session     from sqlmodel import SQLModel, create_engine, Session

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session                  rt random
  
def predict_income():
    base = random.randint(800, 1500)
    trend = random.uniform(0.9, 1.2)      
    return round(base * trend, 2)     api
uvicorn
     
def predict_income():
    base = random.randint(800, 1500)
    trend = random.uniform(0.9, 1.2)
    return round(base * trend, 2)                   ds
2026-03-30 18:22:38.501 [info] update#setState checking for updates
2026-03-30 18:22:39.219 [info] update#setState idle
2026-03-30 19:05:35.796 [warning] No ptyHost heartbeat after 6 seconds
2026-03-30 19:22:38.546 [info] update#setState checking for updates
2026-03-30 19:22:39.333 [info] update#setState idle
2026-03-30 19:28:32.842 [warning] updateWindowsJumpList#setJumpList unexpected result: error

passlib[bcrypt]
