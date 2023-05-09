# 10) Faça um script Python que solicita ao usuário que digite números inteiros indefinidamente e, ao final, 
# digite zero para finalizar a entrada de dados. Os números devem ser inseridos em uma lista à medida em que 
# forem sendo digitados pelo usuário. Ao final transforme todos os números em um único número 
# (ex: [12, 4, 32, 12] = 1243212) e exiba o resultado.

cont = 0
numeros = []

print("Digite números (0 para finalizar)")
while True:
    cont += 1
    numero = int(input(f"Informe o {cont}º número: "))
    if numero == 0:
        break
    numeros.append(numero)

numero = ""
for n in numeros:
    numero += str(n)
numero = int(numero)

print("-=" * 20)
print(f"{numeros} = {numero}")
