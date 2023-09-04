# 7) Faça um script Python que solicite ao usuário que digite uma frase e exiba “Palíndromo” caso a frase seja um palíndromo e “Não é palíndromo” caso não seja. 
# Assuma que a entrada não tem acentos e que todas as letras são minúsculas.
# Obs: Um palíndromo é uma palavra ou frase, que é igual quando lida da esquerda para a direita ou da direita para a esquerda (espaços em brancos são descartados). Exemplos: “ana”, “ovo”, “reviver”.

frase = input("Insira uma string: ").lower()

verificador_1 = []
verificador_2 = []

for letra in frase:
    verificador_1.append(letra)
    verificador_2.insert(0, letra)

if verificador_1 == verificador_2:
    print("Palíndromo")
else:
    print("Não é palíndromo")
