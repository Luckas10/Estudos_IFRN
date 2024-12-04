from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Dialeto do Banco de Dados
engine = create_engine('sqlite:///database.db')

# Sessão do banco de dados
session = Session(bind=engine)

# Declaração para criar uma tabela
declaration = text('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
)
''')

session.execute(declaration)
session.commit()

# Insersão no banco de dados
insert = text('''
    INSERT INTO users(nome) VALUES (:nome)
''')
session.execute(insert, {'nome': 'Enzo'})
session.commit()
