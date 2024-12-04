from sqlalchemy import create_engine, text

# Dialeto do Banco de Dados
engine = create_engine('sqlite:///database.db')

# Conexão com o banco de dados
connection = engine.connect()

# Declaração para criar uma tabela
declaration = text('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
)
''')
connection.execute(declaration)
connection.commit()

# Insersão no banco de dados
insert = text('''
    INSERT INTO users(nome) VALUES (:nome)
''')
connection.execute(insert, {'nome': 'Enzo'})
connection.commit()
