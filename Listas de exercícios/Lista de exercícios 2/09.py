nome = input("Qual é o seu nome? ")
turno = input("Você estuda no turno matutino (M) ou vespertino (V)? ")

if turno == "M":
    print("Bom dia, " + nome + "!")
elif turno == "V":
    print("Boa tarde, " + nome + "!")
else:
    print("Opção inválida.")