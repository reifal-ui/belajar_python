from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Agar remixjs bisa akses api ini jadi menggunakan ini

# Untuk menyimpan todolist di memori sementara
todos = []
next_id = 1

# Untuk mengambil semua todo
@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# Untuk menambahkan todo
@app.route("/api/todos", methods=["POST"])
def add_todo():
    global next_id
    data = request.get_json()

    if not data or 'task' not in data:
        return jsonify({"error": "Task is required"}), 400
    
    new_todo = {
        'id': next_id,
        'task': data['task'],
        'done': False
    }
    todos.append(new_todo)
    next_id += 1
    return jsonify(new_todo), 201

# Untuk menghapus todo berdasarkan id yang ada
@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({"message": "Todo deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)