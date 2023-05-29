# 4) A cantina do campus está oferecendo dois tipos de feijão (feijoada ou feijão verde) e gostaria de saber ao final 
# do dia quantos quilos em média foram consumidos de cada um deles. Para auxiliar nesse levantamento, faça um script 
# Python que tenha apenas 2 registros, contendo cada um deles como chave o tipo de feijão e como valor a quantidade 
# de feijão consumida. O menu do sistema é bem simples:

# *********** Consumo de Feijão na Cantina ***********
# Foram consumidos até o momento aproximadamente: 
# * 0.00 quilos de Feijoada
# * 0.00 quilos de Feijão Verde 
# ****************************************************
# Digite:
# 1 para registrar a venda de um prato de Feijoada
# 2 para registrar a venda de um prato de Feijão Verde

# A cada venda registrada deve ser alterado o valor do registro da quantidade feijão correspondente, incrementando a 
# quantidade em 0.20 quilos.
# Os valores informados na tela principal (menu) devem ser atualizados a cada registro.
# O script só encerra quando o usuário inserir um valor diferente de 1 e 2.

feijoes = {
    "feijoada": 0.00,
    "feijao_verde": 0.00
}
opcao = 1

while opcao == 1 or opcao == 2:
    print("*********** Consumo de Feijão na Cantina ***********")
    print("Foram consumidos até o momento aproximadamente: ")
    print(f"* {feijoes['feijoada']:.2f} quilos de Feijoada")
    print(f"* {feijoes['feijao_verde']:.2f} quilos de Feijão Verde") 
    print("****************************************************")
    print("1 para registrar a venda de um prato de Feijoada")
    print("2 para registrar a venda de um prato de Feijão Verde")
    print("****************************************************")
    opcao = int(input(f"Digite: "))
    
    if opcao == 1:
        feijoes["feijoada"] += 0.2
    if opcao == 2:
        feijoes["feijao_verde"] += 0.2

print("******************************************************")
print("No total, foram consumidos aproximadamente: ")
print(f"* {feijoes['feijoada']:.2f} quilos de Feijoada")
print(f"* {feijoes['feijao_verde']:.2f} quilos de Feijão Verde") 
print("****************************************************")
