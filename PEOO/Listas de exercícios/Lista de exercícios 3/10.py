num = 77
resposta = 0
resposta = int(input("Tente acertar o número de 1 a 100: "))
while not resposta == num:
    if resposta > 100 or resposta < 1:
        resposta = int(input("Insira um número de 1 a 100: "))
    else:
        resposta = int(input("Errou! Tente novamente: "))
print("Acertou! Resposta correta, o número era 77!")