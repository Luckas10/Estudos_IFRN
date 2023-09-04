from tkinter import *

class App:
    def __init__(self) -> None:
        self.janela = Tk()
        self.janela.title("Janela Internacional")
        self.janela.geometry('1280x720')

        self.frame1 = Frame(
            self.janela,
            bg='pink',
            width='1280',
            height='720',
        )
        self.frame1.pack()

        self.botao1 = Button(
            self.frame1,
            text='Clique Aqui!',
            font=('Verdana', '20', 'bold'),
            bg='black',
            fg='white',
        )
        self.botao1.pack()

        self.texto1 = Label(
            self.frame1,
            text='Roberto Carlos',
            bg='black',
            fg='white',
            font=('Arial', '20', 'bold',)
        )
        self.texto1.pack()

        self.janela.mainloop()

janela = App()

