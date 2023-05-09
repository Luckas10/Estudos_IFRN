# 10) Faça um script Python que solicite ao usuário que preencha duas listas com 5 elementos cada. 
# Gere então e exiba uma terceira lista contendo os elementos das duas listas informadas sem elementos repetidos.

lista_1 = []
lista_2 = []
lista_3 = []

print("Preencha a primeira lista com 5 elementos:")
for i in range(0, 5):
    elemento = input(f"Elemento {i + 1}: ")
    lista_1.append(elemento)

print("\nPreencha a segunda lista com 5 elementos:")
for i in range(0, 5):
    elemento = input(f"Elemento {i + 1}: ")
    lista_2.append(elemento)

for elemento_for in lista_1 + lista_2:
    if elemento_for not in lista_3:
        lista_3.append(elemento_for)

print("\nTerceira lista sem elementos repetidos:")
print(lista_3)
