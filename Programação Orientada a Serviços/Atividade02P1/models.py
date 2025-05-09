from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class LivroInput(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int

class Livro(BaseModel):
    id: UUID
    titulo: str
    autor: str
    ano_publicacao: int
    disponibilidade: str  # "disponível" ou "emprestado"

class UsuarioInput(BaseModel):
    nome: str

class Usuario(BaseModel):
    id: UUID
    nome: str
    livros_emprestados: List[UUID]

class EmprestimoInput(BaseModel):
    id_usuario: UUID
    id_livro: UUID

class Emprestimo(BaseModel):
    id: UUID
    id_usuario: UUID
    id_livro: UUID
    data_emprestimo: datetime
    data_devolucao: Optional[datetime]
