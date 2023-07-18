class Carro:
    def __init__(self, cor, nome, marca, vendido):
        self.nome = nome
        self.cor = cor
        self.marca = marca
        self.statusVenda = vendido

    def vendido(self):
        if self.statusVenda:
            print(f"Ele já foi vendido!")
        else:
            print(f"Ele está disponível para a compra!")

Fusca = Carro("azul", "Fusca", "BMW", False)
Camaro = Carro("amarelo", "camaro", "Natura", True)

print("Características do Fusca:")
print(Fusca.vendido())
print(Fusca.nome)
print(Fusca.cor)
print(Fusca.marca)


print(Camaro.vendido())
