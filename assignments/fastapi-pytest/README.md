# 📘 Assignment: Testing FastAPI with pytest

## 🎯 Objective

Write automated tests for a FastAPI task API using pytest and `TestClient`. Practice checking response data, HTTP status codes, and SQLite persistence with an isolated test database.

## 📝 Tasks

### 🛠️ Test Successful API Requests

#### Description

Use the provided API in `app.py` and the starter tests in `test_api.py`. Add tests for listing, creating, retrieving, updating, and deleting tasks. Use a temporary SQLite database so each test starts with isolated data.

#### Requirements

Completed test suite should:

- Use a pytest fixture to set a temporary database path and create a FastAPI `TestClient`.
- Confirm `GET /tasks` returns HTTP 200 and an empty list when the database is empty.
- Confirm `POST /tasks` returns HTTP 201 and the created task has an integer ID and the submitted fields.
- Confirm `GET`, `PUT`, and `DELETE` requests for an existing task return the expected task data and status codes.

### 🛠️ Test Errors and Persistence

#### Description

Add tests for missing task IDs and verify that task data remains available after the API client is restarted with the same database file.

#### Requirements

Completed test suite should:

- Confirm `GET`, `PUT`, and `DELETE` requests for an unknown task ID return HTTP 404.
- Confirm a successful delete returns HTTP 204 and the deleted task can no longer be retrieved.
- Create a task, close the test client, open a new client using the same temporary database, and confirm the task is still available.
- Run successfully with `pytest -q` from this assignment folder.