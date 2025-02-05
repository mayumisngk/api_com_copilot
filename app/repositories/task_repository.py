from typing import List
from app.models.task import Task
from app.memory import Memory

class TaskRepository:
    @staticmethod
    def create_task(task: Task) -> Task:
        Memory.tasks.append(task)
        return task

    @staticmethod
    def list_tasks() -> List[Task]:
        return Memory.tasks

    @staticmethod
    def delete_task(task_id: int):
        Memory.tasks = [task for task in Memory.tasks if task.id != task_id]