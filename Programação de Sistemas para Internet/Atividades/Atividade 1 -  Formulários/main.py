from flask import Flask, request, render_template
from funcoes .funcoes_db import *
import os

app = Flask(__name__)

currentdirectory = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        acompanhantes = int(request.form['acompanhantes'])

        usuarios = listar_usuarios("Inscricoes", "Eventos")
        verificador = False

        numero_inscritos = 0

        for pessoa in usuarios:
            numero_inscritos += int(pessoa[1] + 1)

            if email in pessoa:
                verificador = True

        if verificador:
            return render_template('confirmacao.html', inscritos=numero_inscritos)
        else:
            adicionar_user("Inscricoes", "Eventos",
                           (nome, acompanhantes, email))

            numero_inscritos += 1 + acompanhantes

            return render_template('confirmacao.html', inscritos=numero_inscritos, nome=nome)
        



@app.route('/confirmacao')
def confirmacao():
    return render_template('confirmacao.html')
