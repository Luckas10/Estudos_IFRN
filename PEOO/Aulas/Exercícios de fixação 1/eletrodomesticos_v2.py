class Televisao:
    def __init__(self,canal_inicial=2):
        self.nome = "Não Definido"
        self.ligada = False
        self.canal = canal_inicial
        self.tamanho = 20
        self.marca = "Xing-Ling"
    
    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False
    
    def estado(self):
        if self.ligada:
            return 'Ligada'
        else:
            return 'Desligada'

    def incrementar_canal(self):
        self.canal += 1
    
    def decrementar_canal(self):
        self.canal -= 1
    
    def menu(self):
        print('='*40)
        print('[1] Ligar TV')
        print('[2] Desligar TV')
        print('[3] Incrementar Canal')
        print('[4] Decrementar Canal')
        print('='*40)
        print('Digite a Opção:')
        print('='*40)
    
    def opcao(self,op):
        if op == 1:
            self.ligar()
        elif op == 2:
            self.desligar()
        elif op == 3:
            if self.canal == 99:
                self.canal = 1
            else:
                self.canal +=1
        elif op == 4:
            if self.canal == 1:
                self.canal = 99
            else:
                self.canal -=1
        else:
            pass