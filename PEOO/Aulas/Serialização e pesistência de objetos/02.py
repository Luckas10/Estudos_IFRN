from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("400x400")
        self.janela.title("Editor de textos")

        self.botao1 = Button(
            self.janela, 
            text="Gravar arquivo",
            command=self.ler,
        )
        self.botao1.pack()

        self.caixaDeEdicao1 = Text(self.janela, bg="yellow")
        self.caixaDeEdicao1.pack()

        self.janela.mainloop()

    def ler(self):
        arq = open("texto1.txt", "w")
        texto1 = self.caixaDeEdicao1.get(0.0, END)
        arq.write(texto1)

aplicacao = App()