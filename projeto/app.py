from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "NexusGX"

app.register_blueprint(auth_bp)

@app.route('/')
def index():
    pass

@app.route('/cadastro')
def cadastro():
    pass

@app.route('/login')
def login():
    pass