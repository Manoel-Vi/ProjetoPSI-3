from flask import Flask, render_template
from blueprints.auth import auth_bp
from blueprints.error import error_bp
from blueprints.games import games_bp
from database import Base, engine, SessionLocal
from flask_login import LoginManager
from models import Usuario
from seed import adicionar_admin, adicionar_categorias

app = Flask(__name__)
app.config['SECRET_KEY'] = "NexusGX"

Base.metadata.create_all(bind=engine)

adicionar_admin()
adicionar_categorias()

app.register_blueprint(auth_bp)
app.register_blueprint(error_bp)
app.register_blueprint(games_bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Faça login para acessar esta página."

@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as db:
        return db.get(Usuario, int(user_id))

@app.route('/')
def index():
    return render_template('index.html')
