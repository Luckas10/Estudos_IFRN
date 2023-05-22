# 8) Faça um script Python que solicite a digitação do primeiro nome do usuário e então preencha e exiba uma 
# matriz 4 x 4 contendo as letras do nome informado (uma letra em cada posição) sequencialmente, repetindo o 
# nome até preencher toda a planilha.

matriz_nome = []
cont = 0
print("--" * 25)
nome = str(input("Informe o seu primeiro nome: "))

nome_lista = nome * 16

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(nome_lista[cont])
        cont += 1
    matriz_nome.append(linha)

print("--" * 25)
print("Matriz digitada: ")
print("--" * 25)
for i in range(4):
    print(matriz_nome[i])
