# 4) Faça um script Python que solicita ao usuário a digitação de 5 números e ao final exibe-os 
# no formato de lista mas em ordem crescente.

numeros = []

for i in range(0, 5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

for i in range(0, len(numeros)):
    for j in range(i+1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print("-=" * 20)
print(f"Os números digitados em ordem crescente são: {numeros}")
