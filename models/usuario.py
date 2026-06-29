from database.database import db

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(120), nullable=False)

    usuario = db.Column(db.String(80), unique=True, nullable=False)

    senha = db.Column(db.String(255), nullable=False)

    nivel = db.Column(db.String(20), default="funcionario")

    ativo = db.Column(db.Boolean, default=True)


    def set_senha(self, senha):

        self.senha = generate_password_hash(senha)


    def verificar_senha(self, senha):

        return check_password_hash(self.senha, senha)