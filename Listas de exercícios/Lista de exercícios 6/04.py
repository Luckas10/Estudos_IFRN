#4) Faça um script Python que solicite a digitação dos elementos (números inteiros) de uma matriz 3 x 3 e, 
# ao final, exiba e informe a localização (linha e coluna) do elemento de maior valor da planilha.

matriz = []
maior = 0

print(f"Informe os elementos da matriz 3x3")
print("-" * 25)
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Informe o elemento [{i}]x[{j}]: "))
        if i == j == 0:
            maior = valor
            indice = f"[{i}][{j}]"
        elif valor > maior:
            maior = valor
            indice = f"[{i}][{j}]"
        linha.append(valor)
    matriz.append(linha)

print("-" * 25)
print("Matriz digitada: ")
for i in range(3):
    print(matriz[i])

print("-" * 25)
print(f"Maior elemento encontrado na matriz: {maior}")
print(f"Possição do mairo elemento: {indice}")