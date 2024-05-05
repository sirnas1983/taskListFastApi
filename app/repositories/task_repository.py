from typing import List, Optional
from app.models.task import Task
from app.repositories.base import TaskRepository
from uuid import UUID, uuid4


class InMemoryTaskRepository(TaskRepository):

    def __init__(self):
        self.tasks = []

    def create_task(self, task: Task) -> Task:
        task.id = uuid4()
        self.tasks.append(task)
        return task

    def get_task(self, task_id: UUID) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: UUID, task_data: Task) -> Task:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks[i] = task_data
                return task_data
        raise ValueError("Tarea no encontrada")

    def delete_task(self, task_id: UUID) -> None:
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def list_tasks(self) -> List[Task]:
        return self.tasks
