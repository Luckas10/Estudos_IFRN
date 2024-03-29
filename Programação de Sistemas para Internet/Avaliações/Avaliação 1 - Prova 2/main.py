from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/message-page')
def message_page():
    nome = request.args.get('fname')

    if nome == None:
        nome = "SEM NOME"

    return render_template('message-page.html', name=nome)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')