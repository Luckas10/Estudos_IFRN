# 5) Faça um programa em Python que pede que o usuário informe sua data de nascimento (dia, mês e ano) e, utilizando 
# funções da biblioteca datetime (para saber a data em que o programa está sendo executado) calcule e informe quantos 
# anos o usuário tem.

from datetime import datetime

def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year

    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    return idade


def main():
    print("=== CALCULADOR DE IDADE ===")
    data_nascimento = datetime.strptime(input("Informe sua data de nascimento (DD/MM/AAAA): "), "%d/%m/%Y")
    idade = calcular_idade(data_nascimento)
    print("Você tem", idade, "anos.")


if __name__ == '__main__':
    main()
