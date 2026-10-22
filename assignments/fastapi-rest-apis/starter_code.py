from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    description: Optional[str] = None


class Task(TaskInput):
    id: int


tasks: Dict[int, Task] = {}
next_task_id = 1


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    # TODO: Return all stored tasks.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the task or raise HTTPException with status code 404.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    # TODO: Create a task, assign a unique ID, and store it.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Update the task or raise HTTPException with status code 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Delete the task or raise HTTPException with status code 404.
    return Response(status_code=status.HTTP_204_NO_CONTENT)