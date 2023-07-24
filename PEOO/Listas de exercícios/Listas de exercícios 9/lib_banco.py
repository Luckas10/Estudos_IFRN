from random import randint


class Conta:
    def __init__(self,nome, saldo=0):
        self.cliente_nome = nome
        self.num_conta = None
        self.__saldo = saldo


    def consultar_saldo(self):
        return self.__saldo


    def depositar(self,valor):
        self.__saldo += valor


    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor


    def geraconta(self):
        x = str(randint(0,9))
        for i in range(5):
            x = x + str(randint(0,9))
        return x
    

class ContaCorrente(Conta):
    def __init__(self, nome, saldo, limite=1000):
        super().__init__(nome, saldo)
        self.__limite = limite

    
    def alterar_limite(self, novo_limite):
        self.__limite = novo_limite
    

    def gerar_conta(self):
        return randint(10000, 99999)


class ContaPoupanca(Conta):
    def __init__(self, nome, saldo, taxa_de_juros=0):
        super().__init__(nome, saldo)
        self.__taxa_de_juros = taxa_de_juros


    def set_taxa_de_juros(self, nova_taxa_de_juros):
        self.__taxa_de_juros = nova_taxa_de_juros
        return self.__taxa_de_juros


    def aplicar_juros(self):
        juros = self.consultar_saldo() * self.__taxa_de_juros
        self.depositar(juros)


    def gerar_conta(self):
        return randint(10000, 99999)