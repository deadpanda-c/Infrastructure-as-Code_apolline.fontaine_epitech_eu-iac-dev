from fastapi import FastAPI
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import models
from fastapi.responses import JSONResponse
from models import User

from dependencies import hash_password

from tasks.tasks import router as tasks_router

import os


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # autoriser ces domaines
    allow_credentials=True,
    allow_methods=["*"],              # autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],              # autoriser tous les headers (ex: Authorization)
)

app.include_router(tasks_router)

@app.get("/health")
def healthcheck():
    return JSONResponse(status_code=200, content={"status": "ok"})
