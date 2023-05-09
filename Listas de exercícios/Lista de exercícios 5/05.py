# 5) Faça um script Python que solicite ao usuário que digite uma frase (onde pode utilizar pontos, vírgulas, interrogações, etc… à vontade)
# e então informe o número de palavras contidas na frase inserida.
# Dica: Utilize o método ‘replace’ para remover as pontuações da frase e o método ‘split’ para contar o número de palavras após isso.


pontuacoes = '.,-;?!:_ '
string = input("Insira uma string: ")

for p in pontuacoes:
    if p in string:
        string = string.replace(p, ' ')

tamanho = len(string.split())


print(f"Sem pontuações, a string é {string} e tem {tamanho} palavras.")
