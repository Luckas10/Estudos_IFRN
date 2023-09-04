print("-=" * 25)
print(f"{'APROVADO OU REPROVADO':^50}")
print("-=" * 25)

nota_1 = float(input("Informe a 1° nota: "))
nota_2 = float(input("Informe a 2° nota: "))
media = (nota_1 + nota_2) / 2

print("-=" * 25)
print(f"A média do aluno foi: {media:.2f}")
if media >= 7:
    print("Aluno APROVADO")
else:
    print("Aluno REPROVADO")
