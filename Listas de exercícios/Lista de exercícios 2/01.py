print("-=" * 25)
print(f"{'MAIOR E MENOR':^50}")
print("-=" * 25)

numero_1 = float(input("Informe o 1° número: "))
numero_2 = float(input("Informe o 2° número: "))

print("-=" * 25)
if numero_1 > numero_2:
    print(f"O número {numero_1} é o maior")
elif numero_2 > numero_1:
    print(f"O número {numero_2} é o maior")
else:
    print("Os números são inguais")
