# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend the task API to store data in SQLite, using Python's standard library to learn database tables, SQL queries, and persistent storage.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description

Set up a SQLite database for the task API. The database should be created automatically when the application starts and must keep its data when the server restarts.

#### Requirements

Completed program should:

- Use Python's built-in `sqlite3` module and store data in `tasks.db`.
- Create a `tasks` table with an auto-incrementing integer ID, a required title, and an optional description.
- Create the table only when it does not already exist, so restarting the API does not erase saved tasks.

### 🛠️ Connect the API to SQLite

#### Description

Replace the in-memory task storage with database queries in each REST endpoint. Install the packages listed in `requirements.txt`, then run `uvicorn starter_code:app --reload` from this assignment folder and use `/docs` to test the API.

#### Requirements

Completed program should:

- Use SQLite queries to list, retrieve, create, update, and delete tasks through the existing endpoints.
- Pass user-provided values to SQL statements as parameters rather than building SQL with string formatting.
- Return HTTP 404 when a requested task ID does not exist, HTTP 201 when creating a task, and HTTP 204 when deleting one.
- Keep created tasks available after stopping and restarting the API.