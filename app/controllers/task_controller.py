from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.task import Task
from app.services.task_service import TaskService
from app.repositories.task_repository import InMemoryTaskRepository


router = APIRouter()
task_service = TaskService(InMemoryTaskRepository())


@router.post("/tasks/", response_model=Task)
def create_task(task: Task) -> Task:
    return task_service.create_task(task)


@router.get("/tasks/", response_model=List[Task])
def list_tasks() -> List[Task]:
    return task_service.list_tasks()


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str) -> Task:
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task: Task) -> Task:
    return task_service.update_task(task_id, task)


@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    task_service.delete_task(task_id)
    return {"message": "Task deleted"}
