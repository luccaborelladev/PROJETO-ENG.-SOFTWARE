#App principal com rotas Flask 
 # app.py
from flask import Flask, request, jsonify
from models import db, Task
from flask import render_template  # adicione no topo junto com os imports


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Criar o banco de dados
with app.app_context():
    db.create_all()

# Rota para a página inicial
@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'done': t.done} for t in tasks])

# Rota para adicionar nova tarefa
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'done': new_task.done}), 201

# Rota para atualizar uma tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done})

# Rota para deletar uma tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tarefa deletada com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)

