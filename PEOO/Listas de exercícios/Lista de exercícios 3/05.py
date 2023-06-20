deposito_inicial = float(input("Depósito inicial: R$"))
taxa_juros_mensal = float(input("Insira a taxa de juros mensal: "))
c = 1
while c != 13:
    deposito_inicial += deposito_inicial * taxa_juros_mensal / 100
    print(f"Mês {c}: R${deposito_inicial:.2f}")
    c += 1