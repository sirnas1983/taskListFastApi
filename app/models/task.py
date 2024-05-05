from pydantic import BaseModel, Field
from typing import Optional
import uuid

class Task(BaseModel):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4)
    nombre: str
    fecha_creacion: str
    fecha_vencimiento: str
    observaciones: str
    cumplida: bool
    prioridad: Optional[int] = None
