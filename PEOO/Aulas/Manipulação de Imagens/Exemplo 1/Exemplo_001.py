from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('400x600')
        self.janela.title('Internacional')

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.foto = PhotoImage(file='rk_01.png')

        self.imagem1 = Label(
            self.frame1,
            image=self.foto,
        )
        self.imagem1.pack()

        self.janela.mainloop()


Aplicacao = App()

