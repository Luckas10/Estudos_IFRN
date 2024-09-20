from flask import Flask, render_template, url_for,request,redirect

from flask_login import LoginManager, login_required,login_user, logout_user, current_user

from werkzeug.security import check_password_hash

from models import User, obter_conexao

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERDIFICIL'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def index():
    return render_template('pages/index.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        cpf = request.form['cpf']
        senha = request.form['senha']

        user = User.get_by_email(email)

        if user and check_password_hash(user.cpf, cpf) and check_password_hash(user.senha, senha):
            login_user(user)

            return render_template('pages/dash.html', tipo_usuario=user.tipo_usuario)
        else:
            return render_template('pages/login.html', verificador='Dados incorretos!')
        
    return render_template('pages/login.html')


@app.route('/registro', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        tipo_usuario =  request.form['tipo_usuario']
        nome =  request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        senha = request.form['senha']
        confirmacao_senha = request.form['confirmacao_senha']

        if senha == confirmacao_senha:
            User.insert_user(tipo_usuario, nome, email, cpf, senha)
            return redirect(url_for('login'))
        else:
            return render_template('pages/register.html', status = 'Sua senha está diferente da confirmação')

    return render_template('pages/register.html')


@app.route('/dash')
@login_required
def dash():
    tipo_usuario = request.args.get('tipo_usuario', current_user.tipo_usuario)
    return render_template('pages/dash.html', tipo_usuario=tipo_usuario)


@app.route('/add_tecnologia',methods=['GET','POST'])
def add_tecnologia():
    if request.method=='POST':
        nome =  request.form['nome']
        sigla = request.form['sigla']
        descricao =  request.form['descricao']
        User.insert_tecnologia(nome, sigla, descricao)
        return render_template('pages/dash.html', tipo_usuario=current_user.tipo_usuario, status = 'Tecnologia adicionada')

    return render_template('pages/add_tecnologia.html')


@app.route('/listar_tecnologias', methods=['GET'])
def listar_tecnologias():
    lista = User.listar_tecnologias()
    return render_template('pages/listar_tecnologias.html', lista=lista)



@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))