# 2) Faça um script Python que utilize a mesma string ‘s’ do exercício anterior e exiba como resultado o seu nome e sobrenome.

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.- "

p1 = s[19] + s[24] + s[10] + s[24] + s[-1]
p2 = s[21] + s[-9] + s[12] + s[10] + s[28] + s[-1]
p3 = s[16] + s[24] + s[22] + s[14] + s[28] + s[-1]
p4 = s[13] + s[14] + s[-1]
p5 = s[28] + s[24] + s[-9] + s[-4] + s[10] + s[-3]

print(p1 + p2 + p3 + p4 + p5)