from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('200x100')
        self.janela.title('Internacional')

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.foto1 = PhotoImage(file='btn_ok.png')
        self.foto2 = PhotoImage(file='btn_cancel.png')

        self.botao1 = Button(
            self.frame1,
            image=self.foto1,
            compound='left',
            text='OK',
        )
        self.botao1.pack(side='left')

        self.botao2 = Button(
            self.frame1,
            image=self.foto2,
            compound='left',
            text='Cancel',
        )
        self.botao2.pack(side='left')

        self.janela.mainloop()


Aplicacao = App()
