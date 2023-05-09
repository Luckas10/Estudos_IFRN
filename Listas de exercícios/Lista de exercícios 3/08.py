resposta = 1
int1_25 = 0
int26_50 = 0
int51_75= 0
int76_100 = 0
while resposta != 0:
    resposta = int(input("Insira um número [digite 0 para parar]: "))
    if resposta >= 1 and resposta <=25:
        int1_25 += 1
    elif resposta >= 26 and resposta <=50:
        int26_50 += 1
    elif resposta >= 51 and resposta <=75:
        int51_75 += 1
    elif resposta >= 76 and resposta <=100:
        int76_100 += 1

print(f"{int1_25} números estão entre o intervalo 1-25")
print(f"{int26_50} números estão entre o intervalo 26-50")
print(f"{int51_75} números estão entre o intervalo 51-75")
print(f"{int76_100} números estão entre o intervalo 76-100")