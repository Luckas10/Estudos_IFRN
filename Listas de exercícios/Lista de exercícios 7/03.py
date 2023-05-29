# 3) Faça um script Python que peça para o usuário registrar um estoque de produtos. Cada produto possui um código, 
# um preço e uma quantidade. O estoque pode armazenar 5 produtos. Depois de receber os 5 produtos do estoque, mostre 
# um relatório com os produtos, a quantidade total de itens (todos os produtos) e o valor total do estoque (de todos 
# os produtos).

produto = dict()
estoque = dict()
tot_preco = tot_quantidade = 0

print("-=" * 25)
print("ESTOQUE DE 5 PRODUTOS:")

for i in range(5):
    print("-=" * 25)
    print(f"PRODUTO {i+1}")
    produto["codigo"] = int(input(f"Informe o código: "))
    produto["preco"] = float(input(f"Informe o preço: R$"))
    produto["quantidade"] = int(input(f"Informe a quantidade: "))

    estoque[f"{produto['codigo']}"] = produto.copy()

for k, v in estoque.items():
    for c, n in v.items():
        if c == "preco":
            tot_preco += n
        elif c == "quantidade":
            tot_quantidade += n

print("RELATÓRIO DOS PRODUTOS:")
for k, produto in estoque.items():
    print("-=" * 20)
    print(f"Produto {k}:")
    print("Código |  Preço  | Quantidade ")
    for c, valor in produto.items():
        print(f"{valor}          ", end="")
    print()

print("-=" * 20)
print(f"Total de produtos: {tot_quantidade}")
print(f"Total do valor:    R${tot_preco}")
