from fastapi import APIRouter
from app.api.v1.endpoints import create_task, list_tasks, delete_task

api_router = APIRouter()
api_router.include_router(create_task.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(list_tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(delete_task.router, prefix="/tasks", tags=["tasks"])