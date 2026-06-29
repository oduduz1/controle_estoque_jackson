from flask import Blueprint

from flask import render_template

from flask import request

from flask import redirect

from flask import url_for

from flask import session

from flask import flash

from services.auth_service import AuthService

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]

        senha = request.form["senha"]

        user = AuthService.autenticar(usuario, senha)

        if user:

            session["usuario_id"] = user.id

            session["usuario_nome"] = user.nome

            return redirect("/dashboard")

        flash("Usuário ou senha inválidos")

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/")