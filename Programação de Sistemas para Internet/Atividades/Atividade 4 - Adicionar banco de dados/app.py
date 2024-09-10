from flask import Flask, session, request, \
    render_template, url_for, redirect
from datetime import datetime, timedelta

import sqlite3, jwt, secrets

app = Flask(__name__)

SECRET_KEY = secrets.token_hex(32)

def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    conexao = get_connection()
    usuarios = conexao.execute("SELECT email, senha FROM users").fetchall()
    conexao.close()

    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        senha = request.form['password']

        for usuario in usuarios:
            email_usuario = usuario[0]
            senha_usuario = usuario[1]

            if email == email_usuario:
                if senha == senha_usuario:
                    token = jwt.encode({
                        'user': email,
                        'exp': datetime.utcnow() + timedelta(hours=1)
                    }, SECRET_KEY, algorithm='HS256')


                    return redirect(url_for('dash', token=token))
                else:
                    return "SENHA INCORRETA"

        return "Usuário não cadastrado"

    

@app.route('/register', methods=['GET', 'POST'])
def register():

    conexao = get_connection()
    lista = conexao.execute("SELECT id, email FROM users").fetchall()

    if request.method == 'GET':
        return render_template('register.html')
    else:
        email = request.form['email']
        senha = request.form['password']

        emails_existentes = [user[1] for user in lista]  
        if email in emails_existentes:
            return render_template('login.html')

        SQL = "INSERT INTO users (email, senha) VALUES(?, ?)"
        conexao.execute(SQL, (email, senha))
        conexao.commit()
        conexao.close()
        return redirect(url_for('login'))
    

@app.route('/dash')
def dash():
    token = request.args.get('token')

    if not token:
        return redirect(url_for('index'))

    try:

        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = data['user']
    except jwt.ExpiredSignatureError:
        return "Token expirado, faça login novamente"
    except jwt.InvalidTokenError:
        return "Token inválido, faça login novamente"

    return render_template('dashboard.html', nome=user)

        
@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('index'))
