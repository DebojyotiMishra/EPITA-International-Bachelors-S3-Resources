# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     num1 = request.form.get('num1')
#     num2 = request.form.get('num2')
#     operation = request.form.get('operation')
#     if num1 is None or num2 is None or operation is None:
#         return 'Missing form parameters: num1, num2, and operation are required', 400
#     if operation == 'add':
#         return str(int(num1) + int(num2))
#     elif operation == 'subtract':
#         return str(int(num1) - int(num2))
#     elif operation == 'multiply':
#         return str(int(num1) * int(num2))
#     elif operation == 'divide':
#         if int(num2) == 0:
#             return 'Division by zero error', 400
#         return str(int(num1) / int(num2))
#     else:
#         return 'Invalid operation: operation must be add, subtract, multiply, or divide', 400

# if __name__ == '__main__':
#     app.run(port=8000, debug=True)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json
    if "description" in task and task["description"]:
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "description": task["description"]})
        return jsonify({"message": "Task added", "task": task}), 201
    return jsonify({"message": "Invalid task"}), 400

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)