# 8) Considerando que um servidor público terá um aumento em seu salário de 9%, escreva um script
# Python onde o usuário informa seu salário atual e tem como resposta o seu salário calculado com o
# referido aumento.

print("-" * 21)
print(" CALCULADOR SALARIAL")
print("-" * 21)
salario = float(input("Informe seu salário atual: R$"))
print(f"Seu salário com o aumento de 9%: R${salario + (salario * 0.09)}")
