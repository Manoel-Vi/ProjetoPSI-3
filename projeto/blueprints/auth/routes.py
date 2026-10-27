from flask import redirect, render_template, request, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from blueprints.auth import auth_bp
from models import Usuario
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required
from database import sessionLocal

@auth_bp.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        senha_hash = generate_password_hash(senha)

        usuario = Usuario( 
            nome = nome,
            email = email,
            senha = senha_hash 
        )
        sessionLocal.add(usuario)
        sessionLocal.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')

@auth_bp.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        stmt = select(Usuario).where(Usuario.email == email)
        usuario = sessionLocal.execute(stmt).scalar()

        if usuario and check_password_hash(usuario.senha, senha):
            session.clear()
            session['usuario_id'] = usuario.id

            return redirect(url_for('index'))

    return render_template("auth/login.html")
