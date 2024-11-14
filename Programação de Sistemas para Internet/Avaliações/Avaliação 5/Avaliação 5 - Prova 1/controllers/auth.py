from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User, obter_conexao

auth_bp = Blueprint(
    name='auth', 
    import_name=__name__,
    url_prefix='/auth'
    )

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = User.get_by_email(email)

        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('main.dashboard'))
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        idade = request.form['idade']

        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_usuarios WHERE usr_email = %s", (email,))
        existing_user = cursor.fetchone()
        cursor.close()
        conn.close()

        if existing_user:
            return redirect(url_for('auth.register'))

        senha_hashed = generate_password_hash(senha)
        
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tb_usuarios (usr_email, usr_senha, usr_nome, usr_idade) VALUES (%s, %s, %s, %s)",
                       (email, senha_hashed, nome, idade))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
