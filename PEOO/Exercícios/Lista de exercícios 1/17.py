# 17) Escreva um script Python que receba como entrada dois números (float) e exiba 4 resultados: a
# soma desses números, a subtração do primeiro pelo segundo, a multiplicação entre esses números
# e a divisão do primeiro pelo segundo.

print("--------------------------")
print("      AS 4 OPERAÇÕES      ")
print("--------------------------")

numero_1 = float(input("Informe o 1° valor: "))
numero_2 = float(input("Informe o 2° valor: "))

print("--------------------------")
print(f"Soma:          {numero_1} + {numero_2} = {numero_1 + numero_2}")
print(f"Subtração:     {numero_1} - {numero_2} = {numero_1 - numero_2}")
print(f"Multiplicação: {numero_1} x {numero_2} = {numero_1 * numero_2}")
print(f"Divisão:       {numero_1} / {numero_2} = {numero_1 / numero_2}")
