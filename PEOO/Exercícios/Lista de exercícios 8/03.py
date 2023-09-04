# 3) Faça um programa em Python que utilize funções da biblioteca ‘random’ para criar sugestões de senhas aleatórias. 
# O usuário deve informar o tamanho da senha aleatória e a quantidade de senhas que devem ser geradas. O programa deve 
# então gerar as senhas e criar/gravar no arquivo senhas.txt.

from random import randint

def gerar_senha(tamanho=1, quantidade=1):
    alfabeto_minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabeto_maiuscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '<', '>', ',', '.', '/', '?']
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    arquivo = open("senhas.txt", "a+")

    for c in range(quantidade):
        senha = ""
        for i in range(tamanho):
            escolha1 = randint(1, 4)
            if escolha1 == 1:
                escolha2 = randint(0, len(alfabeto_minuscula)-1)
                senha += alfabeto_minuscula[escolha2]

            elif escolha1 == 2:
                escolha2 = randint(0, len(alfabeto_maiuscula)-1)
                senha += alfabeto_maiuscula[escolha2]

            elif escolha1 == 3:
                escolha2 = randint(0, len(simbolos)-1)
                senha += simbolos[escolha2]
            
            elif escolha1 == 4:
                escolha2 = randint(0, len(numeros)-1)
                senha += numeros[escolha2]

        arquivo.write(f"Senha: {senha}\n")

    arquivo.close()


def exibir_senhas():
    arquivo = open("senhas.txt", "r")
    linhas = arquivo.readlines()
    
    for linha in linhas:
        print(linha)


def main():
    while True:
        print("=== GERADOR DE SENHAS ===")
        print("[1] - Gerar senha")
        print("[2] - Exibir senhas")
        print("[0] - Sair")
        print("=========================")
        opcao = int(input("Informe sua opção: "))
        print("-------------------------")

        if opcao == 0:
            break

        elif opcao == 1:
            tamanho = int(input(f"Informe o tamanho da senha: "))
            quantidade = int(input(f"Informe a quantidade de senhas: "))
            gerar_senha(tamanho, quantidade)

        elif opcao == 2:
            exibir_senhas()

    gerar_senha(tamanho, quantidade)


if __name__ == "__main__":
    main()
