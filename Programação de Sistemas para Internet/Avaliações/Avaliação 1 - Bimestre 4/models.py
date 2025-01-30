from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, Float, DateTime, Table
from datetime import datetime

db = SQLAlchemy()

pedido_produto = Table(
    "pedido_produto",
    db.Model.metadata,
    db.Column("pedido_id", db.Integer, ForeignKey("pedido.id"), primary_key=True),
    db.Column("produto_id", db.Integer, ForeignKey("produto.id"), primary_key=True),
)

class Cliente(db.Model):
    __tablename__ = "cliente"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    rg: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)

    pedidos: Mapped[list["Pedido"]] = relationship(back_populates="cliente")

class Produto(db.Model):
    __tablename__ = "produto"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)

    pedidos: Mapped[list["Pedido"]] = relationship(secondary=pedido_produto, back_populates="produtos")

class Pedido(db.Model):
    __tablename__ = "pedido"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cliente_id: Mapped[int] = mapped_column(Integer, ForeignKey("cliente.id"), nullable=False)
    data_pedido: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    cliente: Mapped["Cliente"] = relationship(back_populates="pedidos")
    produtos: Mapped[list["Produto"]] = relationship(secondary=pedido_produto, back_populates="pedidos")
