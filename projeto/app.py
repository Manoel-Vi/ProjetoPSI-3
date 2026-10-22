from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/cadastro')
def cadastro():
    pass

@app.route('/login')
def login():
    pass