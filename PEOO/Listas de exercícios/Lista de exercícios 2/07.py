num = int(input("Digite um número inteiro positivo: "))

if num % 2 == 0:
    resultado = num ** 2
    print(f"O quadrado de {num} é {resultado}.")
else:
    resultado = num ** 3
    print(f"O cubo de {num} é {resultado}.")