# 7) Faça um script Python que solicite a digitação dos elementos (números inteiros) de duas matrizes 3 x 3 
# e ao final gere e exiba, além das duas matrizes digitadas, uma terceira matriz com os maiores valores de 
# cada posição das matrizes lidas.

matriz_A = []
matriz_B = []
matriz_C = []

print("-" * 25)
print(f"Informe os elementos da matriz A:")
print("-" * 25)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Informe o elemento [{i}]x[{j}]: ")))
    matriz_A.append(linha)

print("-" * 25)
print(f"Informe os elementos da matriz B:")
print("-" * 25)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Informe o elemento [{i}]x[{j}]: ")))
    matriz_B.append(linha)

for i in range(3):
    for j in range(3):
        if matriz_A[i][j] > matriz_B[i][j]:
            matriz_C[i][j] = matriz_A[i][j]
        elif matriz_A[i][j] < matriz_B[i][j]:
            matriz_C[i][j] = matriz_B[i][j]
        else:
            matriz_C[i][j] = matriz_A[i][j]

print("-" * 25)
print(f"Matriz C com os maiores elementos de cada posição:")
print("-" * 25)
for i in range(3):
    print(matriz_C[i])
