import mysql.connector
from flask_login import UserMixin
from config import Config

def obter_conexao():
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )

class User(UserMixin):
    def __init__(self, id, nome, email, senha, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade

    @staticmethod
    def get(user_id):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_usuarios WHERE usr_id = %s", (user_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return User(result[0], result[1], result[2], result[3], result[4])
        return None

    @staticmethod
    def get_by_email(email):
        conn = obter_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_usuarios WHERE usr_email = %s", (email,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return User(result[0], result[1], result[2], result[3], result[4])
        return None
