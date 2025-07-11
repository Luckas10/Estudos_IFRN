#pip install fastapi uvicorn sqlmodel

from sqlmodel import SQLModel, Field
class Aluno(SQLModel, table=True):
    id:int = Field(primary_key=True)
    nome:str = Field(index=False)
    matricula:str=Field(index=False)
    