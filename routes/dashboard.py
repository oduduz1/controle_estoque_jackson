from flask import Blueprint

from flask import render_template

from flask import session

from models.aluguel import Aluguel

from models.cliente import Cliente

from models.maquina import Maquina

from utils.decorators import login_required

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
@login_required
def dashboard():

    return render_template(

        "dashboard.html",

        usuario=session["usuario_nome"],

        total_clientes=Cliente.query.count(),

        total_maquinas=Maquina.query.count(),

        total_alugueis=Aluguel.query.count(),

        alugueis=Aluguel.query.all()

    )