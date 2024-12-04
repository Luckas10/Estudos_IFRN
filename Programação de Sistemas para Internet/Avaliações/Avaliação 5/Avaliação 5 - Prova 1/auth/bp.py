from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, current_user
from users.models import User

auth_bp = Blueprint(
    name='auth', 
    import_name=__name__,
    url_prefix='/auth',
    template_folder='templates'
)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        user = User.find(email=email)
        if user:
            login_user(user)
            return redirect(url_for('users.index'))

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.register'))
