# 13) Considerando que um supermercado dá um desconto de 3% para quem pagar suas compras
# utilizando PIX, escreva um script Python que recebe como entrada o valor das compras de um
# usuário e informa quanto ele pagará se usar o PIX e quanto foi o seu desconto.

print("--------------------------")
print("SUPERMERCADO DO RICARDINHO")
print("--------------------------")

preco = float(input("Informe o valor da sua compra: R$"))
print("""--------------------------
Formas de pagamento: 
[1] Pix = 3% de desconto
[2] À vista = 0% de desconto
--------------------------""")
forma_de_pagamento = int(input("Opção: "))

if forma_de_pagamento == 1:
    print(f"Valor da compra: R${preco}")
    print(f"Valor do desconto: R${preco*0.03}")
    print("--------------------------")
    print(f"Valor total: R${preco - preco*0.03}")
    print("--------------------------")
    print("Chave do pix: 129.215.864-60")
    print("Tipo: CPF")
    print("--------------------------")
    print("Obrigado e volte sempre! :)")

elif forma_de_pagamento == 2:
    print(f"Valor total: R${preco}")
    print("--------------------------")
    print("Obrigado e volte sempre! :)")

else:
    print("ERRO! Opção inválida! Reinicie o sistema.")
