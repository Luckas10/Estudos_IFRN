from tkinter import *

class App:
   def __init__(self):
        self.janela = Tk()
        self.janela.title('Uso do GRID')

        self.nome = Label(self.janela, text='Nome: Ricardo Kleber')
        self.nome.grid(row=0,column=0)

        self.telefone = Label(self.janela, text='Telefone: 84 99888-8888')    
        self.telefone.grid(row=1,column=0)

        self.endereco = Label(self.janela, text='Endereço: Rua da cervejinha')    
        self.endereco.grid(row=2,column=0)

        self.foto = PhotoImage(file='rk_01.png').subsample(3)

        self.imagem1 = Label(self.janela, image=self.foto)
        self.imagem1.grid(row=0, column=1, rowspan=3)

        self.janela.mainloop()

aplicacao=App()
