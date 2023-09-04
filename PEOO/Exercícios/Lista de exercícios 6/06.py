# 6) Faça um script Python que solicite a digitação dos elementos (números inteiros) de uma matriz 3 x 3 
# e calcule e exiba a soma dos elementos da diagonal secundária dessa matriz.

matriz = []
soma_diagonal_secundaria = 0

print("--" * 25)
print(f"Informe os elementos da matriz 3x3:")
print("--" * 25)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Informe o elemento [{i}]x[{j}]: ")))
    matriz.append(linha)

for i in range(3):
    soma_diagonal_secundaria += matriz[i][2-i]

print("--" * 25)
print("Matriz digitada: ")
print("--" * 25)
for i in range(3):
    print(matriz[i])

print("--" * 25)
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")
print("--" * 25)
