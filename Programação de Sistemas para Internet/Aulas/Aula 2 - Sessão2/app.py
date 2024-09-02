from flask import Flask, request, render_template, url_for, session, redirect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'superdificil'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))