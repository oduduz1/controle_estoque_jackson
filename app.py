from flask import Flask

from config import Config

from database.database import db

from models.usuario import Usuario
from models.cliente import Cliente
from models.maquina import Maquina
from models.aluguel import Aluguel


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

from routes.auth import auth
from routes.dashboard import dashboard

app.register_blueprint(auth)
app.register_blueprint(dashboard)

with app.app_context():

    db.create_all()

    if Usuario.query.filter_by(usuario="admin").first() is None:

        admin = Usuario(

            nome="Administrador",

            usuario="admin",

            nivel="Administrador"

        )

        admin.set_senha("123456")

        db.session.add(admin)

        db.session.commit()


if __name__ == "__main__":

    app.run(debug=True)