# 2) Faça um script Python que receba registros inseridos por um usuário com os campos: aluno (string) e media (float) 
# de 0 a 100. A inclusão de registros deve parar quando o usuário digitar ‘pare’ como nome do aluno. Considerando que 
# a média para aprovação é 60, exiba, a partir dos registros, os nomes dos alunos aprovados e, em seguida, os nomes 
# dos alunos reprovados.

alunos = []
alunos_aprovados = []
alunos_reprovados = []

while True:
    nome_aluno = str(input(f"Informe o nome do aluno (ou 'pare' para parar): "))
    if nome_aluno == "pare":
        break

    media = float(input(f"Informe a média de {nome_aluno}: "))

    aluno = {
        "aluno": nome_aluno,
        "media": media
    }

    alunos.append(aluno)

for registro in alunos:
    for k, v in registro.items():
        if k == "media" and v >= 60:
            alunos_aprovados.append(registro["aluno"])
        if k == "media" and v < 60:
            alunos_reprovados.append(registro["aluno"])

print("-=" * 25)
print("Alunos aprovados: ")    
for aluno in alunos_aprovados:
    print(aluno)

print("-=" * 25)
print("Alunos reprovados: ")  
for aluno in alunos_reprovados:
    print(aluno)
