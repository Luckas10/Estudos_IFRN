# 5) Faça um script Python que peça para o usuário entrar com registros de alunos com as seguintes informações: 
# matrícula (inteiro), nome (string), nota1 (float de 0 a 100) e nota2 (float de 0 a 100). Cada registro é armazenado 
# em uma estrutura dicionário + lista (chave = matrícula | valor = lista com os campos nome, nota1 e nota2). O script 
# deve solicitar a entrada de novos registros até que o usuário digite 0 (zero) como matrícula (indicando para o 
# script parar). Nesse momento o script deve informar:
# 
# - Número de alunos matriculados (número de registros)
# - Nome dos alunos matriculados (lista com todos os nomes)
# - Média das notas da 1a Unidade (média dos valores ‘nota1’ dos registros)
# - Média das notas da 2a Unidade (média dos valores ‘nota2’ dos registros)
# - Média final da turma (média aritmética de todas as notas)
# - Lista de alunos aprovados (alunos que tiveram média aritmética acima de 60)

aluno = []
alunos = dict()
cont = 1
soma_nota1 = soma_nota2 = 0

print("-=" * 25)
print(f"{'CADASTRO DE ALUNOS':^50}")
print("-=" * 25)

while True:
    print(f"{cont}° Aluno(a):")
    print("--" * 25)
    matricula = int(input("Matrícula: "))
    if matricula == 0:
        break

    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("1ª Nota: ")))
    aluno.append(float(input("2ª Nota: ")))
    print("--" * 25)
    alunos.update({matricula : aluno})
    aluno = []
    cont += 1

print("-=" * 25)
print("Dados do cadastro: ")
print("-=" * 25)
print(f"Número de alunos matriculados: {len(alunos)}")
print(f"Nome dos alunos matriculados: ")
for valor in alunos.values():
    print(f" - {valor[0]}")
    soma_nota1 += valor[1]
    soma_nota2 += valor[2]

print(f"Média das notas da 1ª Unidade: {(soma_nota1 / len(alunos)):.2f}")
print(f"Média das notas da 2ª Unidade: {(soma_nota2 / len(alunos)):.2f}")
print(f"Média final da turma: {((soma_nota1 + soma_nota2) / (len(alunos) * 2)):.2f}")
print(f"Lista de alunos aprovados: ")
for valor in alunos.values():
    media_aluno = (valor[1] + valor[2]) / 2
    if media_aluno > 60:
        print(f" - Nome: {valor[0]}  |  Média: {media_aluno:.2f}")
    