# 9) Faça um script Python que solicite ao usuário que digite uma frase (sem acentos) e ao final exiba: Quantos espaços em branco existem no texto, 
# e Quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase (sem utilizar acentos): ").lower()
print(f"a: {frase.count('a')}, e: {frase.count('e')}, i: {frase.count('i')}, o: {frase.count('o')}, u: {frase.count('u')} espaços: {frase.count(' ')}")
