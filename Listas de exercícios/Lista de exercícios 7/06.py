# 6) Faça um script Python que crie uma agenda de telefones e e-mails que utilize o ‘nome’ como chave e os demais 
# campos (telefone e e-mails) armazenados como lista no dicionário. O script deve indefinidamente oferecer opções 
# ao usuário, como o menu a seguir, até que o usuário digite 0 (zero) como opção para finalizar.
# Menu da Agenda:

# ******** Agenda em Python *********
#   Existem: 0 contatos cadastrados  
# ***********************************
# 1. Inserir um contato
# 2. Consultar um contato
# 3. Remover um contato
# 4. Listar toda a agenda
# 0. Finalizar
# Digite a opção desejada:

agenda = dict()
contato = list()
cont = 0

while True:
    print("******** Agenda em Python *********")
    print(f"  Existem: {len(agenda)} contatos cadastrados  ")
    print("***********************************")
    print("1. Inserir um contato")
    print("2. Consultar um contato")
    print("3. Remover um contato")
    print("4. Listar toda a agenda")
    print("0. Finalizar")
    print("***********************************")
    opcao = int(input(f"Digite a opção desejada: "))
    print("***********************************")

    if opcao == 0:
    # Sair do programa
        break

    elif opcao == 1:
    # Inserir um novo contato
        nome = str(input(f"Informe o nome do contato: "))
        contato.append(str(input(f"Informe o telefone: ")))
        contato.append(str(input(f"Informe o e-mail: ")))
        agenda.update({nome : contato})
        contato = []

    elif opcao == 2:
    # Consutar um contato
        buscar = str(input("Informe o nome do contato: "))
        print("***********************************")
        for k, v in agenda.items():
            if k == buscar:
                print(f"Dados de {buscar}:")
                print(f"Telefone: {v[0]}")
                print(f"E-mail: {v[1]}")
                cont += 1
        if cont == 0:
            print(f"O nome {buscar} não se encontra na agenda!")
        cont = 0

    elif opcao == 3:
    # Remover um contato
        buscar = str(input("Nome do contato que deseja remover: "))
        print("***********************************")
        if buscar in agenda.keys():
            del agenda[buscar]
            print(f"Contato de {buscar} removido com sucesso!")
        else:
            print(f"O nome {buscar} não se encontra na agenda!")

    elif opcao == 4:
    # Listar toda a agenda
        for k, v in agenda.items():
            print("------------------------------------")
            print(f"Nome: {k}")
            print(f"Telefone: {v[0]}")
            print(f"E-mail: {v[1]}")
            print("------------------------------------")

    else:
        print("ERRO! Digite uma opção válida.")

    