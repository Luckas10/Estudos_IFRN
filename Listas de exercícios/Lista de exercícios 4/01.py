# 1) Faça um script Python que solicita ao usuário a digitação de 5 números inteiros e os 
# armazena em uma lista. Ao final imprime os 5 números seguidos de sua posição na lista.

print("-=" * 20)
lista = []
indices = []
cont = 0

while cont != 5:
    lista.append(int(input(f"Informe o número de índice {cont}: ")))
    indices.append(cont)
    cont += 1

print("-=" * 20)
cont = 0
while cont != len(indices):
    print(f"O número {lista[cont]} está no índice {indices[cont]}")
    cont += 1
