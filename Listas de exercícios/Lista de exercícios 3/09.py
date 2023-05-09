saldo = 1000
print("Você tem um saldo inicial de R$1000,00!")
while saldo != 0:
    compra = float(input("Quanto você vai gastar? R$"))
    while compra > saldo:
        compra = float(input("Você só tem {saldo} de saldo, cuidado! R$"))
    saldo -= compra
    print(f"Saldo: R${saldo}")
print("Acabou o dinheiro!")
