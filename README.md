# ✅ Streamlit To-Do App (Dockerized)

A simple task-tracking web app built with Streamlit and Docker. Add, check, and delete tasks with persistent storage.

## Features
- Add tasks
- Mark tasks as completed
- Delete tasks
- Persistent task storage using `tasks.json`

## Run Locally (Docker)
```bash
docker build -t streamlit-todo-app .
docker run -p 8501:8501 streamlit-todo-app
