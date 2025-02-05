from app.schemas.task import TaskCreate, Task
from app.repositories.task_repository import TaskRepository

class TaskService:
    @staticmethod
    def create_task(task_create: TaskCreate) -> Task:
        task = Task(id=len(TaskRepository.list_tasks()) + 1, **task_create.dict())
        return TaskRepository.create_task(task)

    @staticmethod
    def list_tasks():
        return TaskRepository.list_tasks()

    @staticmethod
    def delete_task(task_id: int):
        TaskRepository.delete_task(task_id)