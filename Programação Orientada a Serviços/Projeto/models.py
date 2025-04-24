from pydantic import BaseModel

class Tarefa(BaseModel):
    id : int
    decricao : str
    prioridade : int
    concluida : bool

