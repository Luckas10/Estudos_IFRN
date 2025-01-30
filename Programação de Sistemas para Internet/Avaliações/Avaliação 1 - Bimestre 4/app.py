from flask import Flask, render_template, request, redirect, url_for
from models import db, Cliente, Produto, Pedido

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        rg = request.form["rg"]
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        novo_cliente = Cliente(rg=rg, nome=nome, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for("clientes"))
    
    clientes = Cliente.query.all()
    return render_template("clientes.html", clientes=clientes)

@app.route("/produtos", methods=["GET", "POST"])
def produtos():
    if request.method == "POST":
        nome = request.form["nome"]
        tipo = request.form["tipo"]
        preco = float(request.form["preco"])
        novo_produto = Produto(nome=nome, tipo=tipo, preco=preco)
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for("produtos"))

    produtos = Produto.query.all()
    return render_template("produtos.html", produtos=produtos)

@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    if request.method == "POST":
        cliente_id = request.form["cliente_id"]
        produtos_ids = request.form.getlist("produtos")
        novo_pedido = Pedido(cliente_id=cliente_id)
        for produto_id in produtos_ids:
            produto = Produto.query.get(produto_id)
            novo_pedido.produtos.append(produto)
        db.session.add(novo_pedido)
        db.session.commit()
        return redirect(url_for("pedidos"))

    clientes = Cliente.query.all()
    produtos = Produto.query.all()
    pedidos = Pedido.query.all()
    return render_template("pedidos.html", clientes=clientes, produtos=produtos, pedidos=pedidos)

if __name__ == "__main__":
    app.run(debug=True)
