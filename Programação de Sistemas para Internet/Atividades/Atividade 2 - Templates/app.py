from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard.html')