from models.cliente import Cliente
from database.database import db


class ClienteService:

    @staticmethod
    def listar():
        return Cliente.query.order_by(Cliente.nome).all()


    @staticmethod
    def buscar(id):
        return Cliente.query.get(id)


    @staticmethod
    def cadastrar(nome, telefone, cnpj, responsavel, email):

        cliente = Cliente(

            nome=nome,

            telefone=telefone,

            cnpj=cnpj,

            responsavel=responsavel,

            email=email

        )

        db.session.add(cliente)

        db.session.commit()


    @staticmethod
    def excluir(id):

        cliente = Cliente.query.get(id)

        if cliente:

            db.session.delete(cliente)

            db.session.commit()