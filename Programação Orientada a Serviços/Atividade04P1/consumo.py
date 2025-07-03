# pip install fastapi uvicorn pydantic requests
import requests

URL = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{URL}/livros")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def cadastrar_livro():
    titulo = input("Digite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a edição: "))

    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }

    r = requests.post(f"{URL}/livros", json=livro)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def excluir_livro(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)
    elif r.status_code == 404:
        print(r.text)

def editar_livro(titulo):
    r_get = requests.get(f"{URL}/livros/{titulo}")
    if r_get.status_code == 200:
        titulo_novo = input("Digite o título: ")
        ano = int(input("Digite o ano: "))
        edicao = int(input("Digite a edição: "))

        livro = {
            "titulo": titulo_novo,
            "ano": ano,
            "edicao": edicao
        }

        r = requests.put(f"{URL}/livros/{titulo}", json=livro)
        if r.status_code == 200:
            print(r.text)
        elif r.status_code == 404:
            print(r.text)

    elif r_get.status_code == 404:
        print(r_get.text)

def menu():
    print("-=-" * 15)
    print("1 - Listar Livros")
    print("2 - Listar Livros pelo título")
    print("3 - Cadastrar Livro")
    print("4 - Deletar Livro")
    print("5 - Editar Livro")
    print("6 - Sair")
    print("-=-" * 15)
    return int(input("Digite sua opção: "))

if __name__ == "__main__":
    opcao = menu()
    while opcao != 6:
        print("-=-" * 15)
        
        if opcao == 1:
            listar_livros()
        elif opcao == 2:
            titulo = input("Digite o título: ")
            listar_livro(titulo)
        elif opcao == 3:
            cadastrar_livro()
        elif opcao == 4:
            titulo = input("Digite o título: ")
            excluir_livro(titulo)
        elif opcao == 5:
            titulo = input("Digite o título: ")
            editar_livro(titulo)

        opcao = menu()