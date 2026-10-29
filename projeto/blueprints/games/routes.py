from flask import render_template
from blueprints.games import games_bp

@games_bp.route('/lista_jogos')
def listar_jogos():
    return render_template("games/listarjogos.html")

@games_bp.route('/lista_pedidos')
def listar_pedidos():
    return render_template("games/listarpedidos.html")