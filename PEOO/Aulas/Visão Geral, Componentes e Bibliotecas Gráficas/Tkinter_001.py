from tkinter import *

class App:

    def __init__(self) -> None:
        self.janela = Tk()
        self.janela.title("Janela Internacional")
        self.janela.geometry('1280x720')

        self.frame1 = Frame(
            self.janela,
            bg='black',
            width='1280',
            height='720',
        )
        self.frame1.pack()

        self.texto1 = Label(
            self.frame1,
            text='Roberto Carlos',
            bg='black',
            fg='white',
            font=('Arial', '20', 'bold',)
        )
        self.texto1.pack()

        self.botao1 = Button(
            self.frame1,
            command=self.muda,
            text='Clique Aqui!',
            font=('Verdana', '20', 'bold'),
            bg='yellow',
            fg='blue',
        )
        self.botao1.pack()

        self.janela.mainloop()

    def muda(self):
        from random import randint

        numero = randint(0, 9)
        lista = ['Olá', 'Bom dia', 'Boa tarde', 'Boa noite', 'Tudo bem?', 'Por favor', 'Bem-vindo', 'Como vai?', 'Estou bem', 'Boa aula']
        self.texto1['text'] = lista[numero]

janela = App()

