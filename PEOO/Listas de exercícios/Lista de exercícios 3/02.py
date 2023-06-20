n1 = int(input("Insira um número inteiro positivo: "))
n2 = int(input("Agora, insira um número maior que o anterior: "))
while not n2 > n1:
    n2 = int(input("Por favor, insira um número maior que o anterior: "))
somador = 0
soma = 0
while not somador == n2:
    somador += 1
    if somador % 2 == 0 and somador >= n1:
        soma += somador
print("A soma é:", soma)