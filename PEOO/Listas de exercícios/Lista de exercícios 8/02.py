# 2) Faça um programa em Python que contenha uma função que recebe uma string e devolve uma outra string de mesmo 
# tamanho alterando cada vogal por um símbolo diferente (defina em sua função os símbolos para cada uma das 5 vogais).
# O programa deve ser estruturado com uma função principal (main) executada quando o programa for rodado e que solicita 
# que o usuário insira strings para serem codificadas pela função até que o usuário digite ‘sair’, encerrando a execução 
# do programa.

def codificar(palavra):
    list_palavra = []

    for letra in palavra:
        temp = letra
        if letra in "Aa":
            temp = "4"
        elif letra in "Ee":
            temp = "3"
        elif letra in "Ii":
            temp = "1"
        elif letra in "Oo":
            temp = "0"
        elif letra in "Uu":
            temp = "V"
        list_palavra.append(temp)

    nova_palavra = ""
    for letra in list_palavra:
        nova_palavra += letra

    return nova_palavra


def main():
    while True:
        print("-----------------------------------------")
        print("Escrava 'sair' para encerrar o programa")
        print("-----------------------------------------")
        palavra = str(input(f"Informe uma palavra para ser codificada: "))

        if palavra == "sair":
            break

        print("-----------------------------------------")
        print(f"Palavra digitada: {palavra}")
        print(f"Palavra codificada: {codificar(palavra)}")
        print("-----------------------------------------")



if __name__ == "__main__":
    main()
