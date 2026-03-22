import os

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

TASKS = []
NEXT_ID = 1


@app.route("/", methods=["GET"])
def index():
    total_tasks = len(TASKS)
    completed_tasks = sum(1 for task in TASKS if task["done"])
    return render_template(
        "index.html",
        tasks=TASKS,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
    )


@app.route("/tasks", methods=["POST"])
def add_task():
    global NEXT_ID

    title = request.form.get("title", "").strip()
    if title:
        TASKS.append({"id": NEXT_ID, "title": title, "done": False})
        NEXT_ID += 1

    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id: int):
    for task in TASKS:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break

    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id: int):
    global TASKS
    TASKS = [task for task in TASKS if task["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "5000"))
    app.run(host=host, port=port, debug=False)
