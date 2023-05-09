# 9) Faça um script Python que solicita ao usuário a digitação de um número inteiro (maior que 1000). 
# Em seguida, transforme o número para string, inverta o número totalmente (ex: 2345 vira 5432), 
# transforme novamente para inteiro, some com 1000 e exiba o resultado.

cont = 4
numero_invertido = ""

while True:
    numero = int(input(f"Informe um número maior que 1000: "))
    if numero < 1000:
        print("Erro!")
    else:
        break

numero = str(numero)
for n in range(3, -1, -1):
    numero_invertido += numero[n]

numero_invertido = int(numero_invertido)
print("-=" * 20)
print(f"Número digitado: {numero}")
print(f"Número invertido: {numero_invertido}")
print(f"Número invertido + 1000: {numero_invertido + 1000}")
