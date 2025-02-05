from fastapi import APIRouter, HTTPException
from app.services.task_service import TaskService

router = APIRouter()

@router.delete("/{task_id}")
def delete_task(task_id: int):
    TaskService.delete_task(task_id)
    return {"message": "Task deleted"}