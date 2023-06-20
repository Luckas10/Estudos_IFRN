# 2) Faça um script Python que solicite a digitação dos elementos (números inteiros) de uma matriz 3 x 3 e, 
# ao final, exiba quantos e quais valores inseridos são maiores que 10.

matriz = []
maior_10 = 0
valores_maior_10 = []

print(f"Informe os elementos da matriz 3x3")
print("-" * 25)
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Informe o elemento [{i}]x[{j}]: "))
        if valor > 10:
            maior_10 += 1
            valores_maior_10.append(valores_maior_10)
        linha.append(valor)
    matriz.append(linha)

print("-" * 25)
print("Matriz digitada: ")
for i in range(3):
    print(matriz[i])

print("-" * 25)
print(f"Número de elementos maiores que 10: {maior_10}")
print(f"Valores maior do que 10: {valores_maior_10}")
