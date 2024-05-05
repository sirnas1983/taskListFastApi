from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.task import Task
from uuid import UUID


class TaskRepository(ABC):
    
    @abstractmethod
    def create_task(self, task: Task) -> Task:
        pass

    @abstractmethod
    def get_task(self, task_id: UUID) -> Optional[Task]:
        pass

    @abstractmethod
    def update_task(self, task_id: UUID, task_data: Task) -> Task:
        pass

    @abstractmethod
    def delete_task(self, task_id: UUID) -> None:
        pass

    @abstractmethod
    def list_tasks(self) -> List[Task]:
        pass
