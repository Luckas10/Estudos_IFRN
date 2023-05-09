# 16) Escreva um script Python que recebe como entrada o valor de uma temperatura em Celsius (C)
# e apresenta como saída o seu valor em Fahrenheit (F).

print("---------------------------")
print("  CONVERSOR DE °C PARA °F  ")
print("---------------------------")

temperatura_C = float(input("Informe a temperatura em °C: "))

print("---------------------------")
print(f"Temperatura em °F: {((9 * temperatura_C) + 160) / 5}")
