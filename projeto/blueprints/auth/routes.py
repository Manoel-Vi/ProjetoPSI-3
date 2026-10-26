from flask import redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from blueprints.auth import auth_bp
from models import Usuario
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required
from database import session

@auth_bp.route('/cadastro', methods=['get', 'post'])
def cadastro():
    if request.method == 'post':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)

        usuario = Usuario( 
            nome = nome,
            email = email,
            senha = senha_hash 
        )
        session.add(usuario)
        session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("auth/login.html")
