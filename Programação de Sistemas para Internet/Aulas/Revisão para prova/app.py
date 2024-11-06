from flask import Flask, render_template
from user import bp as bp_user
from book import bp as bp_book
from emprestimo.bp import bp_emprestimo

app = Flask(__name__)

app.register_blueprint(bp_user)
app.register_blueprint(bp_book)
app.register_blueprint(bp_emprestimo)

@app.route('/')
def index():
    return render_template('index.html')