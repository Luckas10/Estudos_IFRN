# 8) Faça um script Python que solicita ao usuário a digitação do seu primeiro nome, separe as letras
# e armazene no formato de lista  e, em seguida, faça o mesmo com o sobrenome (solicite a digitação e
# armazene em outra lista). Exiba então: o número de letras do nome, o número de letras do sobrenome e
# ao final informe: Seu nome completo é (e exiba o nome completo a partir da concatenação das duas listas).

lista_nome = []
lista_sobrenome = []

nome = str(input(f"Informe seu nome: "))
sobrenome = str(input(f"Informe seu sobrenome: "))

for n in nome:
    lista_nome.append(n)

for s in sobrenome:
    lista_sobrenome.append(s)

print("-=" * 20)
print(f"Seu nome tem {len(lista_nome)} letras")
print(f"Seu sobrenome tem {len(lista_sobrenome)} letras")
print(f"Seu nome completo é: {lista_nome + lista_sobrenome}")
