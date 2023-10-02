from tkinter import *
import pickle

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("400x400")
        self.janela.title("Editor de textos")

        self.botao1 = Button(
            self.janela, 
            text="Ler arquivo",
            command=self.ler,
        )
        self.botao1.pack()

        self.caixaDeEdicao1 = Text(self.janela, bg="yellow")
        self.caixaDeEdicao1.pack()

        self.janela.mainloop()


    def ler(self):
        arq = open("teste.bin", "rb")
        arqDesserializado = pickle.load(arq)
        self.caixaDeEdicao1.insert('0.0', arqDesserializado)

aplicacao = App()