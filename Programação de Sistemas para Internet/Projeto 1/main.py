from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Olá mundo</h1>"


@app.route('/dashboard')
def dashboard():
    dados = {
        'nome' : 'João Lucas Gomes de Souza',
        'cidade' : 'Caico',
        'curso' : 'Informática para à Internet'
    }

    return render_template('dashboard.html', data = dados)


@app.route('/profile')
def profile():
    nome = request.args.get('nome')

    if nome == None:
        nome = "SEM NOME"
    return render_template('profile.html', nome=nome)