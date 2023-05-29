# 7) Faça um script Python que simule um sistema de controle de um posto de gasolina. A cada abastecimento o frentista 
# utiliza o script para informar dados do veículo abastecido. No final do dia o frentista digita 0 (zero) para finalizar 
# o sistema. O menu do sistema de abastecimento deve ser assim:

# ***** Posto Roberto Carlos ******
#   Valor Apurado no DIA: R$ 0.00  
# *********************************
# Registrar Abastecimento:
# Digite a placa do veículo ou 0 para finalizar:

# Em cada registro deve ser informado: 
# Placa do veículo
# Combustível (string: ‘etanol’, ‘gasolina’, ou ‘diesel’)
# Quantidade de litros abastecida (float)

# Quando finalizar (digitar zero) o script deve informar o relatório de abastecimentos:
# Quantidade de carros atendidos
# Quantidade de litros de etanol vendidos
# Quantidade de litros de gasolina vendidos
# Quantidade de litros de diesel vendidos
# Total apurado no dia (considerando que o litro de etanol é R$ 5,00, de gasolina é R$ 6,00 e de diesel é R$ 5,50)

total_carros = list()
valor_apurado = 0
tot_litros_etanol = 0
tot_litros_gasolina = 0
tot_litros_diesel = 0

while True:
    print("***** Posto Roberto Carlos ******")
    print(f"  Valor Apurado no DIA: R$ {valor_apurado}  ")
    print("*********************************")
    print("Registrar Abastecimento: ")

    placa = str(input(f"Digite a placa do veículo ou 0 para finalizar: "))
    if placa == "0":
        break
    combustivel = str(input(f"Digite o combustível abastecido: "))
    quant_litros = float(input(f"Digite a quantidade de litros abastecido: "))
    print("Abastecimento registrado!")
    print("*********************************")

    carro = {
        "placa": placa,
        "combustivel": combustivel,
        "quant_litros": quant_litros
    }
    
    total_carros.append(carro.copy())
    carro = list()

    if combustivel == "etanol":
        valor_apurado += 5.00 * quant_litros
    elif combustivel == "gasolina":
        valor_apurado += 6.00 * quant_litros
    elif combustivel == "diesel":
        valor_apurado += 5.50 * quant_litros

for carro in total_carros:
    if carro['combustivel'] == "etanol":
        tot_litros_etanol += carro['quant_litros']
    elif carro['combustivel'] == "gasolina":
        tot_litros_gasolina += carro['quant_litros']
    elif carro['combustivel'] == "diesel":
        tot_litros_diesel += carro['quant_litros']

print("*********************************")
print("DADOS TOTAIS REGISTRADOS DO DIA:")
print("*********************************")
print(f"Quantidade de litros de etanol vendidos: {tot_litros_etanol}")
print(f"Quantidade de litros de gasolina vendidos: {tot_litros_gasolina}")
print(f"Quantidade de litros de diesel vendidos: {tot_litros_diesel}")
print(f"Total apurado no dia: R${valor_apurado:.2f}")
