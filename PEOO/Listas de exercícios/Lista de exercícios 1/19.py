# 19) O sistema de avaliação de determinada disciplina, é composto por quatro notas. A primeira e a
# segunda tem peso 2, a terceira e a quarta tem peso 3. Faça um script Python que solicita as quatro
# notas de um aluno e calcula a sua média final na disciplina.

print("----------------------------")
print("  CALCULAR MÉDIA PONDERADA  ")
print("----------------------------")

nota_1 = float(input("Informe a 1° nota: "))
nota_2 = float(input("Informe a 2° nota: "))
nota_3 = float(input("Informe a 3° nota: "))
nota_4 = float(input("Informe a 4° nota: "))
media_final = ((nota_1 * 2) + (nota_2 * 2) + (nota_3 * 3 ) + (nota_4 * 3 )) / 10

print("----------------------------")
print(f"Média final: {media_final}")
