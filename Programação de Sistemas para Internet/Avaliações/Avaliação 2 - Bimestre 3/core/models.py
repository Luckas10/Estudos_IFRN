from flask_login import UserMixin
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, Session
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
session = Session(bind=engine)  # Sessão local configurada

class Base(DeclarativeBase):
    pass

class User(Base, UserMixin):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(
        primary_key=True
    )
    email : Mapped[str] = mapped_column(
        nullable=False, 
        unique=True
    )
    nome : Mapped[str] = mapped_column(
        nullable=False,
        unique=True
    )
    senha : Mapped[str] = mapped_column(
        nullable=False
    )

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha