from fastapi import FastAPI
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import User

from fastapi.responses import JSONResponse

from dependencies import hash_password

import os


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@app.on_event("startup")
def create_default_admin():
    db = SessionLocal()
    admin_email = os.getenv("DEFAULT_ADMIN_EMAIL")
    admin_pass = os.getenv("DEFAULT_ADMIN_PASSWORD")

    if not admin_email or not admin_pass:
        print("⚠️ Skipping admin creation: env vars not set.")
        return

    existing_admin = db.query(User).filter(User.email == admin_email).first()
    if not existing_admin:
        hashed_pw = hash_password(admin_pass)
        admin = User(
            email=admin_email,
            username="admin",
            password=hashed_pw,
            is_admin=True,
        )
        db.add(admin)
        db.commit()
        print("✅ Default admin created.")
    else:
        print("ℹ️ Admin already exists.")
    db.close()

origins = [
    "https://codex.techmoulins.fr", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # autoriser ces domaines
    allow_credentials=True,
    allow_methods=["*"],              # autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],              # autoriser tous les headers (ex: Authorization)
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(transaction_router)
app.include_router(team_router)

@app.get("/health")
def healthcheck():
    return JSONResponse(status_code=200, content={"status": "ok"})
