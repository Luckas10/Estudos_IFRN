nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    print("AF")
    rec = float(input("Digite a nota da recuperação: "))
    media_final = (media + rec) / 2
    if media_final >= 5:
        print("Aprovado na recuperação")
    else:
        print("Reprovado na recuperação")
    print(f"Média final: {media_final:.2f}")

#Usei format, mas só pra não ficar com números muito quebrados, sim? :]