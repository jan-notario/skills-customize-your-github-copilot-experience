import sqlite3
from contextlib import asynccontextmanager, contextmanager
from pathlib import Path
from typing import AsyncIterator, Iterator, List, Optional

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

DATABASE_PATH = Path(__file__).with_name("tasks.db")


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


def initialize_database() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT
            )
            """
        )


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    initialize_database()
    yield


app = FastAPI(title="Testable Task API", lifespan=lifespan)


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, description FROM tasks ORDER BY id"
        ).fetchall()
    return [dict(row) for row in rows]


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT id, title, description FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return dict(row)


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (task_input.title, task_input.description),
        )
        row = connection.execute(
            "SELECT id, title, description FROM tasks WHERE id = ?",
            (cursor.lastrowid,),
        ).fetchone()
    return dict(row)


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE tasks SET title = ?, description = ? WHERE id = ?",
            (task_input.title, task_input.description, task_id),
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        row = connection.execute(
            "SELECT id, title, description FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    return dict(row)


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    with get_connection() as connection:
        cursor = connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)