from utils.db import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    estado  = db.Column(db.String(20), nullable=True)
    
    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado