# 1) Crie um programa em Python para implementar uma agenda que guarda registros com os campos: CPF (inteiro), 
# nome (string), telefone (string) em um arquivo chamado agenda.txt. O programa deve conter três funções 
# (para executar as operações solicitadas), além da função principal que disponibiliza as opções (adicionar 
# registro, apagar registro e listar amigos).

def adicionar_registro():
    nome = str(input("Nome: "))
    cpf = int(input("CPF: "))
    telefone = str(input("Telefone: "))
    print("-------------------------")

    agenda = open("agenda.txt", "a+")
    agenda.write(f"{nome};{cpf};{telefone}\n")
    agenda.close()


def deletar_registro():
    cpf = int(input("Informe o CPF a ser removido: "))
    cont = 0

    agenda = open("agenda.txt", "r")
    lines = agenda.readlines()
    agenda.close

    agenda = open("agenda.txt", "w")
    for line in lines:
        amigo = line.split(";")
        if int(amigo[1]) != cpf:
            agenda.write(line)
        else:
            cont += 1
    
    if cont != 0:
        print(f"Registro com o CPF:{cpf} removida!")
    else:
        print(f"Não nenhum registro com o CPF:{cpf}")


def listar_amigos():
    agenda = open("agenda.txt", "r")
    registro = agenda.readlines()
    for amigo in registro:
        nome, cpf, telefone = amigo.strip().split(";")
        print(f"NOME: {nome}")
        print(f"CPF: {cpf}")
        print(f"TELEFONE: {telefone}")
        print("-------------------------")
    agenda.close()


def main():
    while True:
        print("=== AGENDA ELETRÔNICA ===")
        print("[1] - Adicionar registro")
        print("[2] - Deletar registro")
        print("[3] - Listar amigos")
        print("[0] - Sair")
        print("=========================")
        opcao = int(input("Informe sua opção: "))
        print("-------------------------")

        if opcao == 0:
            break
        elif opcao == 1:
            adicionar_registro()
        elif opcao == 2:
            deletar_registro()
        elif opcao == 3:
            listar_amigos()

if __name__ == "__main__":
    main()
