from models.usuario import Usuario
from database.database import db


class AuthService:

    @staticmethod
    def autenticar(usuario, senha):

        user = Usuario.query.filter_by(
            usuario=usuario,
            ativo=True
        ).first()

        if user is None:
            return None

        if not user.verificar_senha(senha):
            return None

        return user