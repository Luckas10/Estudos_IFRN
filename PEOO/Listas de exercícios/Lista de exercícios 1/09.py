# 9) Escreva um script Python que recebe o valor da base e da altura de um triângulo e informa o valor
# de sua área. Dica: A área de um triângulo é igual à multiplicação de sua base x altura / 2.

print("-" * 35)
print("  CALCULAR A ÁREA DE UM TRIÂNGULO")
print("-" * 35)

base = float(input("Informe a base do triâgulo: "))
altura = float(input("Informe a altura do triâgulo: "))
print(f"A área desse triângulo é: {(base*altura)/2}")
