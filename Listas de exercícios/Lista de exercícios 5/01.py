# 1) Execute o script Python abaixo e responda: Qual a mensagem (resultado)?

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- "
i = 14
p1 = s[i] + s[-11] + s[i+14] + s[-25] + s[-1]
p2 = s[25] + s[-5] + s[-10] + s[17] + s[24] + s[23] + s[-1]
p3 = s[-25] + s[i+3] + s[-1]
p4 = s[i+8] + s[-9] + s[i+4] + s[-10] + s[i+10] + s[-1]
p5 = s[-12] + s[i+10] + s[11] + s[i] + s[-12] + s [-10] + s[0] + s[-1]
p6 = s[i-2] + s[10] + s[i+13] + s[21] + s[-15] + s[i+14] + s[-3]
print(p1+p2+p3+p4+p5+p6)

# A mensagem (resultado) exibido é: ESSE PYTHON EH MUITO ROBERTO CARLOS

