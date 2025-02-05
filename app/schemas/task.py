from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class Task(TaskCreate):
    id: int