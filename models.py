#Modelos e DB
# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarefa(db.Model):
    tablename = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "status": self.status
        }