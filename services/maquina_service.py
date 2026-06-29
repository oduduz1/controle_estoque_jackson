from models.maquina import Maquina
from database.database import db


class MaquinaService:

    @staticmethod
    def listar():
        return Maquina.query.order_by(Maquina.nome).all()


    @staticmethod
    def disponiveis():
        return Maquina.query.filter_by(status="Disponível").all()


    @staticmethod
    def cadastrar(nome, modelo, patrimonio, observacao):

        maquina = Maquina(

            nome=nome,

            modelo=modelo,

            patrimonio=patrimonio,

            observacao=observacao

        )

        db.session.add(maquina)

        db.session.commit()


    @staticmethod
    def excluir(id):

        maquina = Maquina.query.get(id)

        if maquina:

            db.session.delete(maquina)

            db.session.commit()