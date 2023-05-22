# 10) Faça um script Python que solicite ao usuário que digite uma palavra qualquer. Em seguida, gere uma matriz 
# quadrada de ordem 4 e preencha os elementos dessa matriz, na sequência, com as letras que compõem a palavra 
# digitada. Terminado o preenchimento dos elementos com a palavra, o script deve então completar os demais 
# elementos da matriz com o caracter ‘X’. Exiba a matriz ao final.

matriz_palavra = []
cont = 0
print("--" * 25)
palavra = str(input("Informe uma palavra: "))

for i in range(4):
    linha = []
    for j in range(4):
        if cont >= len(palavra):
            linha.append("X")
        else:
            linha.append(palavra[cont])
        cont += 1
    matriz_palavra.append(linha)

print("--" * 25)
print("Matriz digitada: ")
print("--" * 25)
for i in range(4):
    print(matriz_palavra[i])