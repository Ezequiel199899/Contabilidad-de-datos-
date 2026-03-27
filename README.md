backend/
 ├── app/
 │   ├── main.py
 │   ├── api.py
 │   ├── auth.py   ✅ (nuevo/reemplazar)
 │   ├── db.py
 │   ├── models.py
 │   ├── api_predict.py.    from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .db import get_session
from .models import User

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
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
        return user.         from .auth import hash_password, verify_password, create_access_token, get_current_user.          t.               from fastapi import APIRouter, Depends
from .auth import get_current_user

router = APIRouter()

@router.post('/predict-summary')
def predict_summary_endpoint(payload: RowsPayload, current_user = Depends(get_current_user)):
    out = predict_summary(payload.rows)
    return {"summaryText": out}.            from fastapi import FastAPI
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
    return {"status": "ok"}.              <!DOCTYPE html>
<html>
<head>
    <title>Finanzas AI</title>
    <style>
        body { font-family: Arial; background:#0f172a; color:white; }
        .card { background:#1e293b; padding:20px; margin:20px; border-radius:10px; }
        input, button { padding:10px; margin:5px; border-radius:5px; }
        button { background:#22c55e; color:white; cursor:pointer; }
    </style>
</head>
<body>

<h1>💰 Finanzas AI</h1>

<div class="card">
    <h3>Registro</h3>
    <input id="email" placeholder="Email">
    <input id="pass" type="password" placeholder="Password">
    <button onclick="register()">Registrarse</button>
</div>

<div class="card">
    <h3>Login</h3>
    <button onclick="login()">Login</button>
</div>

<div class="card">
    <h3>IA</h3>
    <button onclick="runAI()">Analizar</button>
    <pre id="output"></pre>
</div>

<script>
function saveToken(t){ localStorage.setItem('token', t); }
function getToken(){ return localStorage.getItem('token'); }

async function register(){
    const res = await fetch('/auth/register', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({
            email: document.getElementById('email').value,
            password: document.getElementById('pass').value
        })
    });
    const j = await res.json();
    saveToken(j.access_token);
    alert('Registrado');
}

async function login(){
    const res = await fetch('/auth/token', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({
            email: document.getElementById('email').value,
            password: document.getElementById('pass').value
        })
    });
    const j = await res.json();
    saveToken(j.access_token);
    alert('Login OK');
}

async function runAI(){
    const res = await fetch('/predict-summary', {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'Authorization':'Bearer '+getToken()
        },
        body: JSON.stringify({ rows:[{a:1}] })
    });
    const j = await res.json();
    document.getElementById('output').innerText = j.summaryText;
}
</script>

</body>
</html>.     uvicorn app.main:app --reload       