# 8) Faça um script Python que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Exemplo: 15/06/1974 = 15 de junho de 1974.
# OBS: NÃO pode usar bibliotecas, funções ou qualquer método não visto até agora.
# Dica: Utilize o método ‘split’ para separar os campos da data informando ‘/’ como separador.

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

while True: 
    data = str(input("Insira uma data no formado dd/mm/aaaa: "))
    data = data.split('/')

    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])

    if 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 0:
        break
    else:
        print("Insira uma data válida!")

print(f"Dia {dia} de {meses[mes - 1]} de {ano}")
