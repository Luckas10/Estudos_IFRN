from flask import render_template, Blueprint, url_for, request, flash, redirect
from models.user import User
from models.loan import Loan
from models.book import Book


bp = Blueprint('loans', __name__, url_prefix='/loans')

@bp.route('/')
def index():
    return render_template('loans/index.html', loans = Loan.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_id = request.form['user']
        book_id = request.form['book']

        if not user_id or not book_id:
            flash('Usuário e Livro são obrigatórios')
        else:
            loan = Loan(user_id=user_id, book_id=book_id)
            loan.save()
            return redirect(url_for('loans.index'))
    
    users = User.all()
    books = Book.available()
    return render_template('loans/register.html', users=users, books=books)

@bp.route('/return/<int:loan_id>/<int:book_id>')
def return_book(loan_id, book_id):
    Loan.return_book(loan_id, book_id)
    flash('Livro devolvido com sucesso.')
    return redirect(url_for('loans.index'))
