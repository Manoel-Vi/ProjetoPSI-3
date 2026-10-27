from flask import Flask, render_template
from blueprints.auth import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = "NexusGX"

app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    pass

@app.route('/login')
def login():
    pass