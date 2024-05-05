from typing import List, Optional
from app.models.task import Task
from app.repositories.base import TaskRepository
from uuid import UUID


class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, task: Task) -> Task:
        return self.task_repository.create_task(task)

    def get_task(self, task_id: UUID) -> Optional[Task]:
        return self.task_repository.get_task(task_id)

    def update_task(self, task_id: UUID, task_data: Task) -> Task:
        if self.get_task(task_id):
            return self.task_repository.update_task(task_id, task_data)
        else:
            raise ValueError("Task not found")

    def delete_task(self, task_id: UUID) -> None:
        if self.get_task(task_id):
            return self.task_repository.delete_task(task_id)
        else:
            raise ValueError("Task not found")

    def list_tasks(self) -> List[Task]:
        return self.task_repository.list_tasks()
