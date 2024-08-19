from flask import Flask, jsonify, render_template
import pymysql

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'db_escola',
}

# Rota para realizar um SELECT usando código SQL
@app.route('/')
def get_usuario():
    connection = pymysql.connect(**db_config)
   
    try:
        with connection.cursor() as cursor:
            # Executa o comando SQL
            sql = "SELECT * FROM TB_JOGADORES"
            cursor.execute(sql)
            # Obtém todos os resultados
            resultados = cursor.fetchall()
           
            # Converte os resultados em uma lista de dicionários
            usuarios = [{"jog_id": row[0], "jog_nome": row[1], "jog_data_de_nascimento": row[2]} for row in resultados]
   
    finally:
        connection.close()

    return render_template('index.html', dados=usuarios)
    

if __name__ == "__main__":
    app.run(debug=True)