from lib_banco import Conta

while True:
    print("""
    =================================
    (1) Cadastrar Cliente
    (2) Gerar Número da Conta
    (3) Consultar Saldo
    (4) Depositar
    (5) Sacar
    (0) Sair
    =================================
    """)

    opcao = int(input("Digite a Opção: "))
    if opcao == 1:
        nome = str(input("Nome do Cliente: "))
        cliente = Conta(nome)
        print(f"Conta criada no nome de: {cliente.cliente_nome}")

    elif opcao == 2:
        cliente.num_conta = cliente.gerar_conta()
        print("Número da Conta: ")

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 5:
        pass

    elif opcao == 0:
        break
    else:
        print("Errou!!!")

