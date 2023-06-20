print("-=" * 25)
print(f"{'MAIS BARATO':^50}")
print("-=" * 25)

preco_1 = float(input("Informe o 1° preço: R$"))
preco_2 = float(input("Informe o 2° preço: R$"))
preco_3 = float(input("Informe o 3° preço: R$"))

print("-=" * 25)
if preco_1 < preco_2 and preco_1 < preco_3:
    print(f"Compre o produto de preço: R${preco_1}")

if preco_2 < preco_1 and preco_2 < preco_3:
    print(f"Compre o produto de preço: R${preco_2}")

if preco_3 < preco_1 and preco_3 < preco_2:
    print(f"Compre o produto de preço: R${preco_3}")
