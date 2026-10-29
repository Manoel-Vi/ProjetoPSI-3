from flask import redirect, render_template, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from blueprints.auth import auth_bp
from models import Usuario
from sqlalchemy import select
from flask_login import login_user, logout_user, login_required
from database import SessionLocal

@auth_bp.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        db = SessionLocal()
        stmt = select(Usuario).where(Usuario.email == email)
        
        if db.execute(stmt).scalar():
            db.close()
            flash("E-mail já cadastrado!")
            return redirect(url_for('auth.cadastro'))

        senha_hash = generate_password_hash(senha)
        usuario = Usuario(
            nome=nome, 
            email=email, 
            senha=senha_hash
        )

        db.add(usuario)
        db.commit()
        db.close()

        flash("Usuário cadastrado com Sucesso!")
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')

@auth_bp.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        db = SessionLocal()

        stmt = select(Usuario).where(Usuario.email == email)
        usuario = db.execute(stmt).scalar()

        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            flash("Usuário logado com Sucesso!")
            return redirect(url_for('index'))
        else:
            flash("Usuário ou senha inválidos!")
            return redirect(url_for('auth.login'))

    return render_template("auth/login.html")

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Usuário deslogado com Sucesso!")
    return redirect(url_for('index'))

@auth_bp.route('/conta')
@login_required
def conta():
    return render_template("auth/usuario.html")