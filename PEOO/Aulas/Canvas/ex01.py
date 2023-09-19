from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Uso do Canvas')
        self.janela.geometry('720x1280')

        self.canvas1 = Canvas(self.janela)
        self.canvas1.configure()
        self.canvas1.pack()

        self.imagem1 = PhotoImage(file='Iniciante.png').subsample(4)

        self.button1 = Button(self.janela)
        self.button1.configure(
            image=self.imagem1,
            height='73',
            width='333',
            border='0',
        )
        self.button1.place(x=193.5, y=500)

        self.canvas1.create_text(190.5, 400, text='Start Game', fill='black')

        self.janela.mainloop()


janela = App()
