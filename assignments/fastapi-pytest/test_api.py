import pytest
from fastapi.testclient import TestClient

import app as task_api


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(task_api, "DATABASE_PATH", tmp_path / "test_tasks.db")
    with TestClient(task_api.app) as test_client:
        yield test_client


def test_list_tasks_starts_empty(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task_returns_created_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Write tests", "description": "Cover the task API"},
    )

    assert response.status_code == 201
    task = response.json()
    assert isinstance(task["id"], int)
    assert task["title"] == "Write tests"
    assert task["description"] == "Cover the task API"