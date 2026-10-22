import sqlite3
from contextlib import contextmanager
from typing import Iterator, List, Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

DATABASE_PATH = "tasks.db"
app = FastAPI(title="Persistent Task API")


class TaskInput(BaseModel):
    title: str
    description: Optional[str] = None


class Task(TaskInput):
    id: int


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        # TODO: Create the tasks table if it does not already exist.
        pass


initialize_database()


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    # TODO: Select all tasks and convert each database row to a Task.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Select one task by ID or raise HTTPException with status code 404.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    # TODO: Insert the task and return it with its database-generated ID.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Update the task or raise HTTPException with status code 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Delete the task or raise HTTPException with status code 404.
    return Response(status_code=status.HTTP_204_NO_CONTENT)