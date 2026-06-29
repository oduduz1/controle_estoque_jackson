from models.aluguel import Aluguel
from models.maquina import Maquina
from database.database import db


class AluguelService:

    @staticmethod
    def listar():

        return Aluguel.query.all()


    @staticmethod
    def cadastrar(

        cliente,

        maquina,

        inicio,

        fim,

        valor,

        pagamento

    ):

        aluguel = Aluguel(

            cliente_id=cliente,

            maquina_id=maquina,

            data_inicio=inicio,

            data_fim=fim,

            valor=valor,

            status_pagamento=pagamento

        )

        db.session.add(aluguel)

        maq = Maquina.query.get(maquina)

        maq.status = "Alugada"

        db.session.commit()