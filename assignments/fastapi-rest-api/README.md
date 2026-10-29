# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing tasks with FastAPI. Practice defining endpoints, validating request data with Pydantic, and returning appropriate HTTP responses.

## 📝 Tasks

### 🛠️	Create the API and List Tasks

#### Description
Use the provided starter code to run a FastAPI application and implement endpoints for a health check and listing tasks. Store tasks in the in-memory dictionary provided in the starter code.

#### Requirements
Completed program should:

- Start locally with `uvicorn starter-code:app --reload` after installing FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`.
- Return a JSON message from `GET /` to confirm that the API is running.
- Return all tasks as a JSON list from `GET /tasks`.
- Make the interactive API documentation available at `/docs`.


### 🛠️	Create and Retrieve Tasks

#### Description
Add endpoints to create a task and retrieve one task by its ID. Use the provided Pydantic models to validate incoming data.

#### Requirements
Completed program should:

- Create a task with `POST /tasks` using a JSON body such as `{"title": "Read chapter 1"}`.
- Assign each new task a unique integer ID and set its `completed` value to `false` initially.
- Return the created task and use HTTP status code `201` for a successful creation.
- Return a single task from `GET /tasks/{task_id}`.
- Return HTTP status code `404` when the requested task ID does not exist.


### 🛠️	Update and Delete Tasks

#### Description
Complete the API by adding endpoints to replace a task's title and completion state, and to delete a task.

#### Requirements
Completed program should:

- Update a task with `PUT /tasks/{task_id}` using a JSON body containing a non-empty `title` and a `completed` boolean.
- Return the updated task after a successful update.
- Delete a task with `DELETE /tasks/{task_id}` and return a confirmation message.
- Return HTTP status code `404` when an update or delete request uses an unknown task ID.