# 20) Dada a figura abaixo, faça um script Python que calcule o valor hipotenusa (h) seguindo a
# fórmula. O usuário deve entrar com os valores dos dois catetos.

from math import sqrt as raiz

print("----------------------------")
print("  CALCULADOR DE HIPOTENUSA  ")
print("----------------------------")

cateto_oposto = float(input("Valor do cateto oposto: "))
cateto_adjacente = float(input("Valor do cateto adjacente: "))
hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2)) ** (1/2)

print("----------------------------")
print(f"Valor da hipotenusa: {hipotenusa}")
