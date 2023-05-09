# 3) Faça um script Python que solicite ao usuário que informe duas strings e então verifique se a segunda string informada 
# encontra-se dentro da primeira. Se sim, exiba a posição do início da segunda string dentro da primeira.

palavra_1 = input("Digite uma string: ")
palavra_2 = input("Digite outra string: ")

if palavra_2 in palavra_1:
    print(f"A string \"{palavra_2}\" está dentro de \"{palavra_1}\"!, na posição {palavra_1.find(palavra_2)}")
else:
    print(f"A string \"{palavra_2}\" não está dentro de \"{palavra_1}\"!")
