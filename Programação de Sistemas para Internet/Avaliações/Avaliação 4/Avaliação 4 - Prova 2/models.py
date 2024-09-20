from flask_login import UserMixin
import sqlite3

from werkzeug.security import generate_password_hash

BANCO = 'database.db'
def obter_conexao():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    id : str
    def __init__(self, tipo_usuario, nome, email, cpf, senha):
        self.tipo_usuario = tipo_usuario
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha


    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usr_id=?'
        dados = conexao.execute(SELECT, (id,)).fetchone()
        
        if dados:  
            user = User(dados['usr_tipo_usuario'], dados['usr_nome'], dados['usr_email'], dados['usr_cpf'], dados['usr_senha'])
            user.id = dados['usr_id']
            return user
        else:
            return None
        

    @classmethod 
    def get_by_email(cls, email):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usr_email=?'
        dados = conexao.execute(SELECT, (email,)).fetchone()
        if dados != None:
            user = User(dados['usr_tipo_usuario'], dados['usr_nome'], dados['usr_email'], dados['usr_cpf'], dados['usr_senha'])
            user.id = dados['usr_id']
            return user
        else:
            return None
        
    
    @classmethod
    def insert_user(cls, tipo_usuario, nome, email, cpf, senha):
        hash_cpf = generate_password_hash(cpf)
        hash_senha = generate_password_hash(senha)

        conexao = obter_conexao()
        INSERT = 'INSERT INTO tb_usuarios(usr_tipo_usuario, usr_nome, usr_email, usr_cpf, usr_senha) VALUES (?,?,?,?,?)'
        conexao.execute(INSERT,  (tipo_usuario, nome, email, hash_cpf, hash_senha))
        conexao.commit()
        conexao.close()

    
    @classmethod
    def insert_tecnologia(cls, nome, sigla, descricao):

        conexao = obter_conexao()
        INSERT = 'INSERT INTO tb_tecnologias(tec_nome, tec_sigla, tec_descricao) VALUES (?,?,?)'
        conexao.execute(INSERT,  (nome, sigla, descricao))
        conexao.commit()
        conexao.close()

    
    @classmethod
    def listar_tecnologias(cls):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM tb_tecnologias'
        dados = conexao.execute(SELECT).fetchall()
        tecnologias = []

        if dados:
            for dado in dados:
                tecnologias.append(Tecnologia(dado['tec_nome'], dado['tec_sigla'], dado['tec_descricao']))

        return tecnologias


class Tecnologia():
    id: str

    def __init__(self, nome, sigla, descricao):
        self.nome = nome
        self.sigla = sigla
        self.descricao = descricao