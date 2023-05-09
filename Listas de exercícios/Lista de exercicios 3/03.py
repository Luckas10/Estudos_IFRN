fator = int(input("Insira um número inteiro e lhe direi seu valor fatorial: "))
fator_final = fator
fatorial = 1
while fator_final != 0:
    fatorial *= fator_final
    fator_final -= 1

print(f"{fator}! = {fatorial}")