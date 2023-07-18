from random import randint


class Conta:
    def __init__(self, nome):
        self.num_conta = None
        self.cliente_nome = nome
        self.saldo = 0
    

    def depositar(self, valor):
        self.saldo += valor

    
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
    

    def gerar_conta(self):
        x = str(randint(0, 9))
        for i in range(5):
            x += str(randint(0, 9))
        return x