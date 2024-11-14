from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'muitodificil'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable=False)
    senha = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    users = User.query.all()
    return render_template('pages/index.html', users=users)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']
        
        if not email:
            flash('Email é obrigatório')
        else:
            new_user = User(email=email, senha=senha)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('pages/create.html')


@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    user = User.query.get(id)
    
    if user is None:
        return redirect(url_for('error', message='Usuário Inexistente'))

    if request.method == 'POST':
        email = request.form['email']
        user.email = email
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('pages/edit.html', user=user)


@app.route('/error')
def error():
    error = request.args.get('message')
    return render_template('errors/error.html', message=error)


if __name__ == "__main__":
    app.run(debug=True)
