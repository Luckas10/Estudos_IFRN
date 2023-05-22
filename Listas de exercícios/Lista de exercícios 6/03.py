# 3) Faça um script Python que exiba uma matriz 4 x 4 onde o valor de cada elemento da matriz é 
# igual a multiplicação dos seus índices (posição linha x posição coluna). 

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(i * j)
    matriz.append(linha)

print("-" * 25)
print("Matriz (i*j)")
for i in range(4):
    print(matriz[i])

