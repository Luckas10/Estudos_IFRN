from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, User

app = Flask(__name__)
app.secret_key = 'chave-secreta'

# Dialeto do Banco de Dados
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(bind=engine)

# Cria sessão do banco de dados
session = Session(bind=engine)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        
        if nome:  # Verifica se o campo nome não está vazio
            novo_usuario = User(nome=nome)
            session.add(novo_usuario)
            session.commit()
        
        return redirect(url_for('index'))
    
    # Busca todos os usuários cadastrados
    usuarios = session.query(User).all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/remover/<int:id>', methods=['POST'])
def remover(id):
    usuario = session.query(User).get(id)
    if usuario:
        session.delete(usuario)
        session.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    usuario = session.query(User).get(id)
    if request.method == 'POST':
        novo_nome = request.form['nome']
        if usuario and novo_nome:
            usuario.nome = novo_nome
            session.commit()
        return redirect(url_for('index'))
    
    elif request.method == 'GET':
        return render_template('editar.html', usuario=usuario)
