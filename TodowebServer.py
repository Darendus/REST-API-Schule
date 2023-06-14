from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a sample list of todo entries for demonstration purposes
todo_entries = [
    {"id": "1", "title": "Buy groceries", "description": "Milk, bread, eggs", "completed": False},
    {"id": "2", "title": "Walk the dog", "description": "Around the block", "completed": True},
    {"id": "3", "title": "Finish project", "description": "Complete all tasks", "completed": False}
]

# Define the GET endpoint for /todo-list/{list_id}
@app.route('/todo-list/<string:list_id>', methods=['GET'])
def get_todo_list(list_id):
    # Filter the todo entries by list_id
    filtered_entries = [entry for entry in todo_entries if entry.get('list_id') == list_id]

    # If no entries are found, return a 404 error
    if not filtered_entries:
        return jsonify({"message": "Todo list with the given ID not found"}), 404

    # Otherwise, return the filtered entries
    return jsonify(filtered_entries), 200

# Define the DELETE endpoint for /todo-list/{list_id}
@app.route('/todo-list/<string:list_id>', methods=['DELETE'])
def delete_todo_list(list_id):
    # Filter the todo entries by list_id and remove them from the list
    global todo_entries
    todo_entries = [entry for entry in todo_entries if entry.get('list_id') != list_id]

    # If no entries were removed, return a 404 error
    if len(todo_entries) == len(filtered_entries):
        return jsonify({"message": "Todo list with the given ID not found"}), 404

    # Otherwise, return a success message
    return jsonify({"message": "List and all entries were successfully deleted"}), 200

# Define the PATCH endpoint for /todo-list/{list_id}
@app.route('/todo-list/<string:list_id>', methods=['PATCH'])
def update_todo_list(list_id):
    # Find the todo entry with the given list_id
    entry = next((entry for entry in todo_entries if entry.get('list_id') == list_id), None)

    # If no entry is found, return a 404 error
    if not entry:
        return jsonify({"message": "List not found"}), 404

    # Otherwise, update the entry with the new name
    data = request.get_json()
    name = data.get('name')
    entry['name'] = name

    # Return a success message
    return jsonify({"message": "List successfully updated"}), 200
@app.route('/todo-list', methods=['GET'])
def get_todo_lists():
    return jsonify(todo_lists)

@app.route('/todo-list', methods=['POST'])
def create_todo_list():
    data = request.get_json()
    name = data['name']
    new_todo_list = {
        'id': str(uuid.uuid4()),
        'name': name
    }
    todo_lists.append(new_todo_list)
    return jsonify(new_todo_list), 200