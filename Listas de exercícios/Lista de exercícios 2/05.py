a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a < b + c and b < a + c and c < a + b:
    print("Estes valores podem ser os lados de um triângulo.")
else:
    print("Estes valores não podem ser os lados de um triângulo.")