from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, User

# Dialeto do Banco de Dados
engine = create_engine('sqlite:///database.db')

# Criar o banco de dados
Base.metadata.create_all(bind=engine)

# Cria sessão do banco de dados
session = Session(bind=engine)

# Adição no banco de dados
user = User(nome='Melissa')
user = User(nome='Kohara')

session.add(user)
session.commit()