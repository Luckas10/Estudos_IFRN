# 5) Faça um script Python que solicita ao usuário e armazena em uma lista quatro notas e ao final apresenta: 
# a média aritmética, a maior nota e a menor nota.

notas = []
soma = 0

for i in range(0, 4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota
    notas.append(nota)

for n in range(0, 4):
    if n == 0:
        maior = notas[n]
        menor = notas[n]
    else:
        if notas[n] > maior:
            maior = notas[n]
        if notas[n] < menor:
            menor = notas[n]

print("-=" * 20)
print(f"Notas informadas: {notas}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média aritmética: {soma / 4}")
