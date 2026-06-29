from database.database import db


class Maquina(db.Model):

    __tablename__ = "maquinas"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(120), nullable=False)

    modelo = db.Column(db.String(100))

    patrimonio = db.Column(db.String(50))

    status = db.Column(

        db.String(30),

        default="Disponível"

    )

    observacao = db.Column(db.Text)

    alugueis = db.relationship(

        "Aluguel",

        backref="maquina",

        lazy=True

    )