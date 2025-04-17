import streamlit as st
import json
import os

TASKS_FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

# Main App
st.title("✅ Streamlit To-Do App (Dockerized)")
st.write("Track your tasks and stay productive! 🚀")

# Load tasks
tasks = load_tasks()

# Add new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task.strip():
        tasks.append({"task": new_task.strip(), "done": False})
        save_tasks(tasks)
        st.rerun()

# Display and manage tasks
if tasks:
    st.write("### Your Tasks:")
    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.05, 0.8, 0.15])
        tasks[i]["done"] = col1.checkbox("", value=task["done"], key=f"chk_{i}")
        col2.write(f"~~{task['task']}~~" if task["done"] else task["task"])
        if col3.button("❌", key=f"del_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.rerun()

# Save any checkbox updates
save_tasks(tasks)
