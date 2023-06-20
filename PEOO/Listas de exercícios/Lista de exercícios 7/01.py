# 1) Faça uma agenda utilizando um script Python para armazenar 5 registros (nome/telefone) informados pelo usuário 
# em uma lista de dicionários. Em seguida, exiba os 5 registros (um por linha).

agenda = []

for i in range(5):
    nome = str(input(f"Digite o Nome a acrescentar: "))
    telefone = str(input(f"Telefone de {nome}: "))

    dicionario = {
        "nome": nome,
        "telefone": telefone
    }

    agenda.append(dicionario)


for registro in agenda:
    print(registro)
