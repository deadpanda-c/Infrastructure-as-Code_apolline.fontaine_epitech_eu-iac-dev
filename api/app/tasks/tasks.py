from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db
from fastapi.security import OAuth2PasswordBearer

from dependencies import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get("/test")
def test():
    return {"test": "test"}


