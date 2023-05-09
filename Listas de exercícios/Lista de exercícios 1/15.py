# 15) Escreva um script Python onde o usuário informa a velocidade média que o seu carro (em km/h)
# geralmente corre em uma viagem e a quilometragem (em km) até o destino e tem como resposta em
# quantas horas ele levará para fazer a sua viagem.
print("--------------------------")
print("      HORAS DE VIAGEM     ")
print("--------------------------")

velocidade = float(input("Informe a velocidade média (em Km/h): "))
quilometragem = float(input("Informe a quilometragem (em Km): "))

print("--------------------------")
print(f"Sua viagem irá demorar {quilometragem / velocidade} horas.")
