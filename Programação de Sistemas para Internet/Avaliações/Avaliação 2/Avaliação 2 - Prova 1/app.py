from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

# Lista global para armazenar mensagens
mensagens = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        resp = make_response(redirect(url_for('mensagens_view')))
        resp.set_cookie('username', username)
        return resp
    return render_template('login.html')

@app.route('/mensagens', methods=['GET', 'POST'])
def mensagens_view():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        mensagem = request.form['mensagem']
        if username not in mensagens:
            mensagens[username] = []
        mensagens[username].append(mensagem)
    
    user_msgs = mensagens.get(username, [])
    return render_template('mensagens.html', lista_mensagem=user_msgs)

if __name__ == '__main__':
    app.run(debug=True)