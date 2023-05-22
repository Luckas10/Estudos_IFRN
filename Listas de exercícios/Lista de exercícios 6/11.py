# 11) Faça um script Python que, inicialmente, define duas matrizes quadradas de ordem 5 (de nomes ‘vogais’ e
# ‘consoantes’) contendo a primeira em sua diagonal principal as vogais do alfabeto ( e os demais elementos
# iguais a zero) e a segunda em ordem crescente sequencial as consoantes (complementada, também, com zeros),
# como ilustrado a seguir:

# Em seguida o script armazena em uma LISTA o SEU PRIMEIRO NOME (cada letra como um elemento da lista)
# construída a partir das letras das duas matrizes definidas inicialmente.
# Exemplo: A Lista nome = [‘R’,‘I’,‘C’,‘A’,‘R’,‘D’,‘O’] deve ser construída pelo script Python buscando
# nas matrizes seus elementos selecionados da seguinte forma:
# ‘R’ = Matriz ‘consoantes’ posição (2,3)
# ‘I’ = Matriz ‘vogais’ posição (2,2)
# ‘C’ = Matriz ‘consoantes’ posição (0,1)
# ‘A’ = Matriz ‘vogais’ posição (0,0)
# ‘R’ = Matriz ‘consoantes’ posição (2,3)
# ‘D’ = Matriz ‘consoantes’ posição (0,2)
# ‘O’ = Matriz ‘vogais’ posição (3,3)
# Ao final, exiba a lista ‘nome’ construída.

vogais = [["A", 0, 0, 0, 0],
          [0, "E", 0, 0, 0],
          [0, 0, "I", 0, 0],
          [0, 0, 0, "O", 0],
          [0, 0, 0, 0, "U"]]

consoantes = [["B", "C", "D", "F", "G"],
              ["H", "J", "K", "L", "M"],
              ["N", "P", "Q", "R", "S"],
              ["T", "V", "W", "X", "Y"],
              ["Z", 0, 0, 0, 0]]

print("--" * 25)
nome = "LUCAS"
lista = []

for i in range(len(nome)):
    for l in range(5):
        for c in range(5):
            if nome[i] == consoantes[l][c]:
                print(f"'{nome[i]}' = Matriz 'consoantes' posição ({l}, {c})")
                lista.append(nome[i])

    for l in range(5):
        for c in range(5):
            if nome[i] == vogais[l][c]:
                print(f"'{nome[i]}' = Matriz 'vogais' posição ({l}, {c})")
                lista.append(nome[i])

print("--" * 25)
print(lista)
