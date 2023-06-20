print("-=" * 25)
print(f"{'ORDEM CRESCENTE':^50}")
print("-=" * 25)

number_1 = float(input("Informe o 1° número: "))
number_2 = float(input("Informe o 2° número: "))
number_3 = float(input("Informe o 3° número: "))

print("-=" * 25)
if number_1 < number_2 and number_1 < number_3:
    print(number_1)
    if number_2 < number_3:
        print(number_2)
        print(number_3)
    if number_3 < number_2:
        print(number_3)
        print(number_2)


if number_2 < number_1 and number_2 < number_3:
    print(number_2)
    if number_1 < number_3:
        print(number_1)
        print(number_3)
    if number_3 < number_1:
        print(number_3)
        print(number_1)

if number_3 < number_2 and number_3 < number_1:
    print(number_3)
    if number_1 < number_2:
        print(number_1)
        print(number_2)
    if number_2 < number_1:
        print(number_2)
        print(number_1)
    