from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# Initial data
todos = [
    {
        "id": uuid.uuid4().hex,
        "title": "Learn Python",
        "description": "Learn Python programming language",
        "done": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Buy groceries",
        "description": "Buy groceries for dinner",
        "done": False,
    },
]
# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
# Get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# Get single todo
@app.route("/todos/<string:todo_id>", methods=["GET"])
def get_todo_by_id(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return jsonify(todo)
    return jsonify({"message": "Todo not found"}), 404

# Create a todo
@app.route("/todos", methods=["POST"])
def create_todo():
    title = request.json.get("title", "")
    description = request.json.get("description", "")
    done = False
    todo = {
        "id": uuid.uuid4().hex,
        "title": title,
        "description": description,
        "done": done,
    }
    todos.append(todo)
    return jsonify(todo), 201

# Update a todo
@app.route("/todos/<string:todo_id>", methods=["PUT"])
def update_todo_by_id(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            title = request.json.get("title", todo["title"])
            description = request.json.get("description", todo["description"])
            done = request.json.get("done", todo["done"])
            todo["title"] = title
            todo["description"] = description
            todo["done"] = done
            return jsonify(todo)
    return jsonify({"message": "Todo not found"}), 404

# Delete a todo
@app.route("/todos/<string:todo_id>", methods=["DELETE"])
def delete_todo_by_id(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return jsonify({"message": "Todo deleted"})
    return jsonify({"message": "Todo not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)