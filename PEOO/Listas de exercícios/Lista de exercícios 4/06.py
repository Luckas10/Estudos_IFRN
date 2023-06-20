# 6) Faça um script Python que solicita ao usuário a digitação de 5 números, armazena-os em uma lista e, 
# em seguida, solicita ao usuário que digite um número. O script deve então consultar e informar se o 
# número está ou não na lista.

numeros = []
verificador = False

for i in range(0, 5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

print("-=" * 20)
numero = int(input(f"Informe outro número: "))

print("-=" * 20)
for i in numeros:
    if i == numero:
        verificador = True

if verificador == True:
    print(f"O número {numero} está na lista {numeros}")
else:
    print(f"O número {numero} não está na lista {numeros}")
    