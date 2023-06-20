# 7) Faça um script Python que imprima na tela os números de 1 a 20, um abaixo do outro e, em seguida, 
# no formato de lista (um ao lado do outro, entre colchetes, separados por vírgula)

numeros = []

for i in range(1, 21):
    print(i)
    numeros.append(i)

print("-=" * 20)
print(numeros)
