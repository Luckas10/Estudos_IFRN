from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/pagina1')
def pagina1():


    return render_template('pagina1.html')


@app.route('/pagina2')
def pagina2():


    return render_template('pagina2.html')


@app.route('/pagina3')
def pagina3():


    return render_template('pagina3.html')