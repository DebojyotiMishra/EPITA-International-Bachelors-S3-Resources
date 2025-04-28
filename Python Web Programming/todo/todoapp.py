from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route("/addtask")
def addTask():
    new_task = Task(description="Task 1", completed=False)
    db.session.add(new_task)
    db.session.commit()
    tasks = Task.query.all()
    return render_template("display.html", tasks=tasks)

@app.route("/updatetask")
def updateTask():
    task = Task.query.get(1)
    task.completed = True
    db.session.commit()
    tasks = Task.query.all()
    return render_template("display.html", tasks=tasks)

@app.route("/deletetask")
def deleteTask():
    task = Task.query.get(1)
    db.session.delete(task)
    db.session.commit()
    tasks = Task.query.all()
    return render_template("display.html", tasks=tasks)

@app.route("/display")
def display():
    tasks = Task.query.all()
    return render_template("display.html", tasks=tasks)

# In-memory storage for tasks
tasks = []
next_id = 1  # To track the next task ID

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    global next_id
    description = request.form.get("description")
    if not description:
        return "Task description cannot be empty.", 400
    task = {"id": next_id, "description": description, "completed": False}
    tasks.append(task)
    next_id += 1
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)

