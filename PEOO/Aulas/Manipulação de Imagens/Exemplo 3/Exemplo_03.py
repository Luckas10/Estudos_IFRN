from tkinter import *
from PIL import ImageTk, Image 

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Internacional')

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.imagemCarregada = ImageTk.PhotoImage(Image.open('luffy rebaixado.jpg'))

        self.imagem1 = Label(
            self.frame1,
            image=self.imagemCarregada,
        )
        self.imagem1.pack()

        self.janela.mainloop()


Aplicacao = App()
