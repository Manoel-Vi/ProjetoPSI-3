from flask import redirect, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from auth import auth_bp

@auth_bp.route('/cadastro', methods=['get', 'post'])
def cadastro():
    if request.method == 'post':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)
