from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, Task
from app.services.task_service import TaskService

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(task: TaskCreate):
    return TaskService.create_task(task)