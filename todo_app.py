from flask import Flask, render_template, request, redirect, jsonify
import os

app = Flask(__name__)

DATA_FILE = 'todos.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        f.write('[]')  # Initialize with empty list

@app.route('/')
def index():
    with open(DATA_FILE, 'r') as f:
        todos = f.read()  # Read todos from local storage
    return render_template('todo.html', todos=json.loads(todos))

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        with open(DATA_FILE, 'r') as f:
            todos = json.load(f)
        todos.append(todo)
        with open(DATA_FILE, 'w') as f:
            json.dump(todos, f)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_todo():
    todo = request.form.get('todo')
    if todo:
        with open(DATA_FILE, 'r') as f:
            todos = json.load(f)
        todos.remove(todo)
        with open(DATA_FILE, 'w') as f:
            json.dump(todos, f)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)