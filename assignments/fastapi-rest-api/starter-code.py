from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: dict[int, Task] = {}