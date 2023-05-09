while True:
    nome = str(input("Informe seu nome: "))
    if len(nome) <= 3:
        print("Insira um nome com mais de 3 letras.")
    else:
        break

while True:
    idade = int(input("Informe sua idade: "))
    if idade < 10:
        print("Insira uma idade entre 10 e 100 anos.")
    else:
        break

while True:
    estado_civil = str(input("Informe seu estado civil: ")).upper()
    if estado_civil == "S" or estado_civil == "C" or estado_civil == "D" or estado_civil == "V":
        if estado_civil == "S":
            estado_civil == "Solteiro (a)"
        elif estado_civil == "C":
            estado_civil == "Casado (a)"
        elif estado_civil == "D":
            estado_civil == "Solteiro (a)"
        elif estado_civil == "V":
            estado_civil == "Solteiro (a)"
        break
    else:
        print("Insira as letras: S, C, D ou V")

while True:
    telefone = str(input("Informe seu telefone: "))
    if len(telefone) == 9:
        break
    else:
        print("Insira um telefone com 9 dígitos.")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Estado civil: {estado_civil}")
print(f"Telefone: {telefone}")
