from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(
        primary_key=True
    )
    nome : Mapped[str]

class Book(Base):
    __tablename__ = 'books'
    id : Mapped[int] = mapped_column(
        primary_key=True
    )
    nome : Mapped[str] = mapped_column(
        unique=True
    )