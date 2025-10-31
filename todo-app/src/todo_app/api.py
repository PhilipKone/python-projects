from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for To-Do items
todo_items = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todo_items), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    todo_items.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id < 0 or todo_id >= len(todo_items):
        return jsonify({'error': 'Todo not found'}), 404
    todo_items[todo_id] = request.json
    return jsonify(todo_items[todo_id]), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id < 0 or todo_id >= len(todo_items):
        return jsonify({'error': 'Todo not found'}), 404
    deleted_todo = todo_items.pop(todo_id)
    return jsonify(deleted_todo), 200

if __name__ == '__main__':
    app.run(debug=True)