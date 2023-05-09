est1 = float(input("Digite a primeira estatura: "))
est2 = float(input("Digite a segunda estatura: "))
est3 = float(input("Digite a terceira estatura: "))

if est1 == est2 or est1 == est3 or est2 == est3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura.")
else:
    maior = est1
    if est2 > maior:
        maior = est2
    if est3 > maior:
        maior = est3
    print("A maior estatura é:", maior)