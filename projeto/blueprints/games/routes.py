from flask import render_template, flash
from blueprints.games import games_bp
from flask_login import login_required, current_user
from database import SessionLocal
from sqlalchemy import select
from models import Jogo, Categoria, jogo_categoria, Pedido
from collections import defaultdict

@games_bp.route('/lista_jogos')
@login_required
def listar_jogos():
    db = SessionLocal()

    stmt = (
        select(Jogo, Categoria)
        .join(Pedido, Pedido.id_jogo == Jogo.id)
        .join(jogo_categoria, jogo_categoria.c.jogo_id == Jogo.id)
        .join(Categoria, Categoria.id == jogo_categoria.c.categoria_id)
        .where(Pedido.id_usuario == current_user.id)
    )

    resultados = db.execute(stmt).all()
    jogos_dict = defaultdict(list)

    for jogo, categoria in resultados:
        if categoria not in jogos_dict[jogo]:
            jogos_dict[jogo].append(categoria)

    if not resultados:
        flash("Ainda não possui jogos na sua lista...")

    return render_template("games/listarjogos.html", jogos=jogos_dict)

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