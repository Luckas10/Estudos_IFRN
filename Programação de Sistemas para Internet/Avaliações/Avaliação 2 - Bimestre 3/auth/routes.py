from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from core.models import User, session, engine, Base

auth_bp = Blueprint('auth', 'auth', template_folder='templates')
Base.metadata.create_all(bind=engine)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        nome = request.form['nome']
        senha = request.form['senha']
        user = session.query(User).filter_by(nome=nome).first()

        if user.nome and user.senha == senha:
            login_user(user)
            usuarios = session.query(User).all()
            return render_template('core/users.html', usuarios = usuarios)

    return render_template('login.html')


@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        user = User(email=email, nome=nome, senha=senha)
        session.add(user)
        session.commit()

        return redirect(url_for('auth.login'))
  
    return render_template('register.html')



@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))