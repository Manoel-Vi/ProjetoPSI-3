from flask import render_template, flash, redirect, url_for
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
    db = SessionLocal()

    stmt = (
        select(Pedido, Jogo)
        .join(Jogo, Pedido.id_jogo == Jogo.id)
        .where(Pedido.id_usuario == current_user.id)
    )
    pedidos = db.execute(stmt).all()
    db.close()

    return render_template("games/listarpedidos.html", pedidos=pedidos)

@games_bp.route('/adicionar_pedido/<int:id_jogo>', methods=['POST'])
@login_required
def adicionar_pedido(id_jogo):
    db = SessionLocal()
    jogo = db.get(Jogo, id_jogo)

    if not jogo:
        db.close()
        flash("Jogo não encontrado.")
        return redirect(url_for('games.biblioteca'))

    pedido = Pedido(id_usuario=current_user.id, id_jogo=jogo.id)
    nome_jogo = jogo.nome
    db.add(pedido)
    db.commit()
    db.close()

    flash(f"{nome_jogo} foi adicionado aos pedidos!")
    return redirect(url_for('games.biblioteca'))

@games_bp.route('/biblioteca')
@login_required
def biblioteca():
    db = SessionLocal()

    stmt = select(Jogo)
    jogos = db.scalars(stmt).all()

    db.close()

    return render_template("games/biblioteca.html", jogos=jogos)