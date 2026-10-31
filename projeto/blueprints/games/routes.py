from flask import render_template
from blueprints.games import games_bp
from flask_login import login_required
from database import SessionLocal
from sqlalchemy import select
from models import Jogo

@games_bp.route('/lista_jogos')
@login_required
def listar_jogos():
    return render_template("games/listarjogos.html")

@games_bp.route('/lista_pedidos')
@login_required
def listar_pedidos():
    return render_template("games/listarpedidos.html")

@games_bp.route('/biblioteca')
@login_required
def biblioteca():
    db = SessionLocal()

    stmt = select(Jogo)
    jogos = db.scalars(stmt).all()

    db.close()

    return render_template("games/biblioteca.html", jogos=jogos)