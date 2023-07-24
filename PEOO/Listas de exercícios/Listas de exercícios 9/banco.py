from lib_banco import ContaCorrente, ContaPoupanca
import os


def cadastrar_cliente():
    cliente_nome = input("Digite o cliente_nome do cliente: ")
    saldo_corrente = float(input("Digite o saldo inicial da conta corrente: "))
    conta_corrente = ContaCorrente(cliente_nome, saldo_corrente)

    saldo_poupanca = float(input("Digite o saldo inicial da conta poupança: "))
    taxa_de_juros = float(input("Digite a taxa de juros da conta poupança (em decimal): "))
    conta_poupanca = ContaPoupanca(cliente_nome, saldo_poupanca, taxa_de_juros)
    return conta_corrente, conta_poupanca


def main():
    conta_corrente, conta_poupanca = None, None 

    while True:
        print('''
        =======================================
        Banco Internacional
        =======================================
        [1] Cadastrar Cliente
        [2] Gerar Número da Conta
        [3] Consultar Saldo
        [4] Depositar
        [5] Sacar
        [6] Aplicar Juros (Conta Poupança)
        [0] Sair
        ''')

        opcao = int(input('Informe a Opção: '))

        if opcao == 1:
            os.system('cls')
            conta_corrente, conta_poupanca = cadastrar_cliente() 

            os.system('cls')
            print(f'Cliente Cadastrado: {conta_corrente.cliente_nome}')

        elif opcao == 2:
            os.system('cls')
            if conta_corrente is not None and conta_poupanca is not None:
                conta_corrente.num_conta = conta_corrente.gerar_conta()
                conta_poupanca.num_conta = conta_poupanca.gerar_conta()
                print(f'Cliente: {conta_corrente.cliente_nome} | Número da Conta Corrente: {conta_corrente.num_conta}')
                print(f'Cliente: {conta_poupanca.cliente_nome} | Número da Conta Poupança: {conta_poupanca.num_conta}')
            else:
                print('Nenhum cliente cadastrado. Cadastre um cliente primeiro.')

        elif opcao == 3:
            os.system('cls')
            if conta_corrente is not None and conta_poupanca is not None:
                print(f'Cliente: {conta_corrente.cliente_nome} | Número da Conta Corrente: {conta_corrente.num_conta} | Saldo Corrente: {conta_corrente.consultar_saldo()}')
                print(f'Cliente: {conta_poupanca.cliente_nome} | Número da Conta Poupança: {conta_poupanca.num_conta} | Saldo Poupança: {conta_poupanca.consultar_saldo()}')
            else:
                print('Nenhum cliente cadastrado. Cadastre um cliente primeiro.')

        elif opcao == 4:
            os.system('cls')
            if conta_corrente is not None and conta_poupanca is not None:
                valor = float(input(f'Valor a Depositar para {conta_corrente.cliente_nome} : '))
                escolha_conta = input("Digite 'corrente' para conta corrente ou 'poupança' para conta poupança: ")
                if escolha_conta == 'corrente':
                    conta_corrente.depositar(valor)
                elif escolha_conta == 'poupança':
                    conta_poupanca.depositar(valor)
                else:
                    print("Escolha inválida.")
            else:
                print('Nenhum cliente cadastrado. Cadastre um cliente primeiro.')

        elif opcao == 5:
            os.system('cls')
            if conta_corrente is not None and conta_poupanca is not None:
                valor = float(input(f'Valor a Sacar da conta de {conta_corrente.cliente_nome} : '))
                escolha_conta = input("Digite 'corrente' para conta corrente ou 'poupança' para conta poupança: ")
                if escolha_conta == 'corrente':
                    conta_corrente.sacar(valor)
                elif escolha_conta == 'poupança':
                    conta_poupanca.sacar(valor)
                else:
                    print("Escolha inválida.")
            else:
                print('Nenhum cliente cadastrado. Cadastre um cliente primeiro.')

        elif opcao == 6:
            os.system('cls')
            if conta_poupanca is not None:
                conta_poupanca.aplicar_juros()
                print(f"Juros aplicados na Conta Poupança de {conta_poupanca.cliente_nome}.")
            else:
                print('Nenhum cliente cadastrado. Cadastre um cliente com conta poupança primeiro.')

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()