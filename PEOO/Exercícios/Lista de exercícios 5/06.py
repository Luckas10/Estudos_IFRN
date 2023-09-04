# 6) Faça um script Python que solicite ao usuário que digite um número e exiba “Palíndromo” caso o número digitado seja um palíndromo e “Não é palíndromo” 
# caso não seja. Obs: Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplos: 121, 12321.

numero = int(input("Insira um número: "))

if numero == numero[::-1]:
    print("Palíndromo")
else:
    print("Não é palíndromo")
