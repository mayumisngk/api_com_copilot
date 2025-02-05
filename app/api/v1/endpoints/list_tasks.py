from fastapi import APIRouter
from typing import List
from app.schemas.task import Task
from app.services.task_service import TaskService

router = APIRouter()

@router.get("/", response_model=List[Task])
def list_tasks():
    return TaskService.list_tasks()