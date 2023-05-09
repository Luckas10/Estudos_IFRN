# 18) Escreva um script Python que calcula o IMC (Índice de Massa Corporal) de uma pessoa. Para
# isso o script deve solicitar o peso e a altura do usuário e informar seu IMC ( a fórmula do IMC =
# massa x altura²)

# Obs: Ricardo, você errou a fórmula do IMC, ao invés de (massa x altura²), o certo é (massa / altura²)
# Escrito por João Lucas :)

print("---------------------------")
print("     CALCULADOR DE IMC     ")
print("---------------------------")

massa = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (m): "))

print("---------------------------")
print(f"Seu IMC (Índice de Massa Corporal) é: {massa / altura**2 :.2f}")
