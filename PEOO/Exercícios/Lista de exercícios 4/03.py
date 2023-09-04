# 3) Faça um script Python que solicita ao usuário a digitação de 10 números e ao final exibe-os
# no formato de lista mas em ordem inversa.

print("-=" * 20)
lista = []
lista_reversa = []
cont = 0

while cont != 10:
    lista.append(int(input(f"Informe o número de índice {cont}: ")))
    cont += 1

print("-=" * 20)
cont = 9
while cont != -1:
    lista_reversa.append(lista[cont])
    cont -= 1

print(f"Lista digitada: {lista}")
print(f"Lista reversa:  {lista_reversa}")
