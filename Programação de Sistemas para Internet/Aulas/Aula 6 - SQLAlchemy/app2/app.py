from sqlalchemy import create_engine, text

# Dialeto do Banco de Dados
engine = create_engine('mysql+mysqldb://root:@localhost/novo')

# Conexão com o banco de dados
connection = engine.connect()

# Declaração para criar uma tabela
declaration = text('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(45)
)
''')
connection.execute(declaration)
connection.commit()
