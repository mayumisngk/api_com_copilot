def get_memory_storage():
    # This function will return the in-memory storage for tasks
    return []


def get_task_repository():
    # This function will return the task repository instance
    from app.repositories.task_repository import TaskRepository
    return TaskRepository(get_memory_storage())