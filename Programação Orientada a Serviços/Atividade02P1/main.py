from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from models import Livro, Usuario, Emprestimo, LivroInput, UsuarioInput, EmprestimoInput

app = FastAPI()

livros: List[Livro] = []
usuarios: List[Usuario] = []
emprestimos: List[Emprestimo] = []

@app.post("/cadastrar_livro/", response_model=Livro)
def cadastrar_livro(livro_input: LivroInput):
    livro = Livro(
        id=uuid4(),
        titulo=livro_input.titulo,
        autor=livro_input.autor,
        ano_publicacao=livro_input.ano_publicacao,
        disponibilidade="disponível"
    )
    livros.append(livro)
    print(f"[LOG] Livro cadastrado: {livro.titulo}")
    return livro

@app.get("/livros/", response_model=List[Livro])
def listar_livros(disponivel: bool = None):
    if disponivel is None:
        return livros
    elif disponivel:
        livros_emprestados = []
        for livro in livros:
            if livro.disponibilidade == "emprestado":
                livros_emprestados.append(livro)
        return livros_emprestados
    else:
        livros_emprestados = []
        for livro in livros:
            if livro.disponibilidade == "emprestado":
                livros_emprestados.append(livro)
        return livros_emprestados


@app.get("/livros/{titulo}", response_model=Livro)
def buscar_livro_por_titulo(titulo: str):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():  
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.post("/cadastrar_usuario/", response_model=Usuario)
def cadastrar_usuario(usuario_input: UsuarioInput):
    usuario = Usuario(
        id=uuid4(),
        nome=usuario_input.nome,
        livros_emprestados=[]
    )
    usuarios.append(usuario)
    print(f"[LOG] Usuário cadastrado: {usuario.nome}")
    return usuario

@app.post("/realizar_emprestimo/", response_model=Emprestimo)
def realizar_emprestimo(dados: EmprestimoInput):
    usuario = None
    for u in usuarios:
        if u.id == dados.id_usuario:
            usuario = u
            break
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    livro = None
    for l in livros:
        if l.id == dados.id_livro:
            livro = l
            break
        
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")

    if livro.disponibilidade != "disponível":
        raise HTTPException(status_code=400, detail="Livro não está disponível.")

    livro.disponibilidade = "emprestado"
    usuario.livros_emprestados.append(livro.id)

    emprestimo = Emprestimo(
        id=uuid4(),
        id_livro=livro.id,
        id_usuario=usuario.id,
        data_emprestimo=datetime.now(),
        data_devolucao=None
    )
    emprestimos.append(emprestimo)
    print(f"[LOG] Empréstimo realizado: Livro '{livro.titulo}' para {usuario.nome}")
    return emprestimo

@app.post("/registrar_devolucao/", response_model=Emprestimo)
def registrar_devolucao(id_usuario: UUID, id_livro: UUID):
    usuario = None
    for u in usuarios:
        if u.id == id_usuario:
            usuario = u
            break

    livro = None
    for l in livros:
        if l.id == id_livro:
            livro = l
            break

    if not usuario or not livro:
        raise HTTPException(status_code=404, detail="Usuário ou livro não encontrado.")

    emprestimo = None
    for e in emprestimos:
        if e.id_usuario == id_usuario and e.id_livro == id_livro and e.data_devolucao is None:
            emprestimo = e
            break

    if not emprestimo:
        raise HTTPException(status_code=400, detail="Empréstimo ativo não encontrado.")

    emprestimo.data_devolucao = datetime.now()
    livro.disponibilidade = "disponível"
    if livro.id in usuario.livros_emprestados:
        usuario.livros_emprestados.remove(livro.id)

    print(f"[LOG] Livro devolvido: '{livro.titulo}' por {usuario.nome}")
    return emprestimo

@app.get("/usuario/{id_usuario}/livros_emprestados", response_model=List[Livro])
def listar_livros_emprestados(id_usuario: UUID):
    usuario = None
    for u in usuarios:
        if u.id == id_usuario:
            usuario = u
            break

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    livros_emprestados = []
    for livro in livros:
        if livro.id in usuario.livros_emprestados:
            livros_emprestados.append(livro)

    return livros_emprestados

@app.get("/historico_emprestimos/", response_model=List[Emprestimo])
def listar_historico():
    return emprestimos
