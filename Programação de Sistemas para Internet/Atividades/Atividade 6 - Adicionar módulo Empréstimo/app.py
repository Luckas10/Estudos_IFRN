import os
from flask import Flask
from controllers import users, books, loans

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(loans.bp)
