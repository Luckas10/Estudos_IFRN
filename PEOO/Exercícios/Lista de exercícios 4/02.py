# 2) Faça um script Python que solicita ao usuário a digitação de 5 números inteiros e os armazena em uma lista. 
# Ao final imprime o maior e o menor número digitados seguidos de sua posição na lista.

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
    if cont == 0:
        maior = lista[cont]
        indice = cont
    else:
        if lista[cont] > maior:
            maior = lista[cont]
            indice = cont

    cont += 1

print(f"O maior número digitado foi {maior} no índice {indice}")