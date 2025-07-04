import requests

URL = "http://127.0.0.1:8000"

def buscar_pedido_por_id():
    id_pedido = input("Digite o ID do pedido: ").strip()
    r = requests.get(f"{URL}/pedido/{id_pedido}")

    print("-=-" * 15)
    if r.status_code == 200:
        pedido = r.json()
        print("📋 Dados do Pedido:\n")
        for chave, valor in pedido.items():
            print(f"{chave}: {valor}")
    elif r.status_code == 404:
        print("Pedido não encontrado (Erro 404)")

def menu():
    print("-=-" * 15)
    print("1 - Buscar Pedido por ID")
    print("2 - Sair")
    print("-=-" * 15)
    return int(input("Digite sua opção: "))

if __name__ == "__main__":
    opcao = menu()
    while opcao != 2:
        print("-=-" * 15)

        if opcao == 1:
            buscar_pedido_por_id()

        opcao = menu()
