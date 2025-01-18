from flask import Flask, request, render_template, redirect, url_for
from database import db, init_db
from database.models import User, Book

app = Flask(__name__)
app.config.from_object('database.config.Config')

# Inicializa o banco de dados
init_db(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_user.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published_year = request.form['published_year']
        book = Book(title=title, author=author, published_year=published_year)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_book.html')

@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return render_template('list_users.html', users=users)

@app.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    return render_template('list_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
