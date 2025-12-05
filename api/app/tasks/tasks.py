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


@router.get("/")
def read_tasks():
  return {"tasks": ["task1", "task2"]}

@router.get("/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
  return {"task": f"task {task_id}"}

@router.post("/")
def create_task():
  return {"task": "task created"}

@router.put("/{task_id}")
def update_task():
  return {"task": "task updated"}

@router.delete("/{task_id}")
def delete_task():
  return {"task": "task deleted"}
