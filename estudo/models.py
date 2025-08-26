from estudo import db
from datetime import datetime


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    respondido = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return f'<Contato: {self.nome}>'
