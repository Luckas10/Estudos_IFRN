# 14) Escreva um script Python que receba como entrada um preço de uma mercadoria e o valor
# percentual ofertado como desconto por um lojista e informe qual o preço com desconto.

print("--------------------------")
print("SUPERMERCADO DO RICARDINHO")
print("--------------------------")

valor_da_compra = float(input("Valor da compra: R$"))
desconto_ofertado = float(input("Informe o desconto ofertado: "))

print("--------------------------")
print(f"Valor da compra: R${valor_da_compra}")
print(f"Valor do desconto: R${(valor_da_compra*desconto_ofertado) / 100}")
print("--------------------------")
print(f"Valor total: R${valor_da_compra - ((valor_da_compra*desconto_ofertado) / 100)}")
print("--------------------------")
print("Chave do pix: 129.215.864-60")
print("Tipo: CPF")
print("--------------------------")
print("Obrigado e volte sempre! :)")