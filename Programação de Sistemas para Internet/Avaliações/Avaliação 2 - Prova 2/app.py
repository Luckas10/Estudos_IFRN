from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)

usuarios = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome_usuario = request.form['nome']
        resp = make_response(redirect(url_for('add_result')))
        resp.set_cookie('usuario', nome_usuario)
        if nome_usuario not in usuarios:
            usuarios[nome_usuario] = []
        return resp
    return render_template('login.html')


@app.route('/add_result', methods=['GET', 'POST'])
def add_result():
    usuario = request.cookies.get('usuario')
    if not usuario:
        return redirect(url_for('login'))

    if request.method == 'POST':
        distancia = request.form['distancia']
        tempo = request.form['tempo']
        if usuario in usuarios:
            usuarios[usuario].append((distancia, tempo))
        return redirect(url_for('results'))

    return render_template('add_result.html')


@app.route('/results')
def results():
    usuario = request.cookies.get('usuario')
    if not usuario:
        return redirect(url_for('login'))

    resultados = usuarios.get(usuario, [])
    return render_template('results.html', resultados=resultados)


@app.route('/filtro/<usuario>')
def filtro(usuario):
    usuario = request.cookies.get('usuario')
    if not usuario:
        return redirect(url_for('login'))

    resultados = usuarios.get(usuario, [])
    return render_template('filtro.html', resultados=resultados, dado=usuario)



if __name__ == '__main__':
    app.run(debug=True)


