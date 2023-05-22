# 9) Faça um script Python que solicite a digitação dos elementos (letras quaisquer do alfabeto) de uma matriz 
# 3 x 3 e ao final exiba a matriz, insira as letras da diagonal principal em uma lista e, finalmente, exiba 
# essa lista.

matriz = []
diagonal_principal = []

print("--" * 25)
print(f"Informe os elementos da matriz 3x3:")
print("--" * 25)
for i in range(3):
    linha = []
    for j in range(3):
        valor = str(input(f"Informe o elemento [{i}]x[{j}]: "))
        linha.append(valor)
        if i == j:
            diagonal_principal.append(valor)
    matriz.append(linha)

print("--" * 25)
print("Matriz digitada: ")
print("--" * 25)
for i in range(3):
    print(matriz[i])

print("--" * 25)
print("Lista da diagonal principal:")
print(diagonal_principal)
print("--" * 25)
