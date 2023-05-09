resposta = 1
soma_pares = 0
soma_impares = 0
while resposta != 0:
    resposta = int(input("Insira um número [digite 0 para parar]: "))
    if resposta % 2 == 0:
        soma_pares += resposta
    else:
        soma_impares += resposta

print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")