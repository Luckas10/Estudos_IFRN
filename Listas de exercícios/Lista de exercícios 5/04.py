# 4) Faça um script Python que solicite ao usuário que informe uma string e então informe quantas vezes cada letra/caractere 
# que a compõe aparece na string. Não diferencie maiúsculas e minúsculas.

letras = "abcdefghijklmnopqrstuvwxyz"
resposta = input("Insira uma string: ").lower()

for l in letras:
    if resposta.count(l) > 0:
        print(f"A letra \"{l}\" aparece {resposta.count(l)} vezes na string!")
        