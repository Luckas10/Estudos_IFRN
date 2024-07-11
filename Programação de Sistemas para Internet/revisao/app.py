from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Oi"


@app.route('/render')
def render():
    return render_template('index.html')


@app.route('/dados')
def dados():
    nome = "Romerito, the best em ser o the best"
    return render_template('dados.html', nome=nome)


@app.route('/formulario', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('formulario.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        return nome
        # return render_template('dados.html', nome=nome)