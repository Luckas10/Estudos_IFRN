from flask import Flask, render_template, url_for, request, Blueprint, redirect
from books.models import Book
from users.models import User
from flask_login import login_required

bp = Blueprint('books', __name__, url_prefix='/books', template_folder='templates')

@bp.route('/')
@login_required
def index():
    return render_template('books/index.html', books = Book.all())

@bp.route('/register', methods=['POST', 'GET'])
@login_required
def register():
    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']

        book = Book(titulo, user)
        book.save()
        return redirect(url_for('books.index'))


    return render_template('books/register.html', users=User.all())