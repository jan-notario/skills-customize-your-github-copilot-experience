# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API in Python with FastAPI, practicing HTTP methods, request validation, and status codes.

## 📝 Tasks

### 🛠️ Create Task Endpoints

#### Description

Complete the starter code to create an in-memory API for managing tasks. Install the packages listed in `requirements.txt`, then run the API with `uvicorn starter_code:app --reload` and use the interactive documentation at `/docs` to try the endpoints.

#### Requirements

Completed program should:

- Define a `TaskInput` model with a required `title` and an optional `description`.
- Return all tasks with `GET /tasks`.
- Return one task with `GET /tasks/{task_id}`, or an HTTP 404 response if it does not exist.
- Create a task with `POST /tasks`, assign it a unique integer ID, and return HTTP 201.

### 🛠️ Update and Delete Tasks

#### Description

Add endpoints to update or remove a task, handling requests for task IDs that are not in the in-memory store.

#### Requirements

Completed program should:

- Update a task with `PUT /tasks/{task_id}` and return the updated task.
- Return HTTP 404 when an update or delete request uses an unknown task ID.
- Delete a task with `DELETE /tasks/{task_id}` and return HTTP 204 when successful.
- Use `/docs` to test each endpoint and confirm the returned data and status codes.