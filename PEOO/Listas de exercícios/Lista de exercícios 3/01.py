resposta = 1
soma = 0
cont = 0

while not resposta == 0:
    resposta = int(input("Insira um número [digite 0 para parar]: "))
    soma += resposta
    if resposta == 0:
        break
    cont += 1
print("A média foi:", soma / cont)
