from database.database import db


class Aluguel(db.Model):

    __tablename__ = "alugueis"

    id = db.Column(db.Integer, primary_key=True)

    cliente_id = db.Column(

        db.Integer,

        db.ForeignKey("clientes.id"),

        nullable=False

    )

    maquina_id = db.Column(

        db.Integer,

        db.ForeignKey("maquinas.id"),

        nullable=False

    )

    data_inicio = db.Column(db.Date)

    data_fim = db.Column(db.Date)

    valor = db.Column(db.Float)

    status_pagamento = db.Column(

        db.String(20),

        default="Pendente"

    )

    status = db.Column(

        db.String(20),

        default="Ativo"

    )