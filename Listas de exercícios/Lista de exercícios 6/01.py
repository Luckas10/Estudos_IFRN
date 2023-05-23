# 1) Faça um script Python que peça para o usuário entrar com o número de linhas (m), colunas (n) e os 
# elementos (números inteiros) de uma matriz A e depois calcule e mostre a matriz B, tal que B é igual 
# à transposta de A (AT).
# OBS: Matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma dada matriz.

matriz = []
matriz_t = []

print("Dados da matriz: ")
print("-" * 25)
linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

print(f"Informe os elementos da matriz {linhas}x{colunas}")
print("-" * 25)
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Informe o elemento [{i}]x[{j}]: ")))
    matriz.append(linha)

for i in range(colunas):
    matriz_t.append([0] * linhas)

for i in range(linhas):
    for j in range(colunas):
        matriz_t[j][i] = matriz[i][j]

print("-" * 25)
print("Matriz digitada: ")
for i in range(linhas):
    print(matriz[i])

print("Matriz transposta:")
for j in range(colunas):
    print(matriz_t[j])