from tkinter import *


from tkinter import *

class App:

    def __init__(self) -> None:
        self.janela = Tk()
        self.janela.title("Janela Internacional")
        self.janela.geometry('250x200')

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.texto1 = Label(
            self.frame1,
            text='Nome',
        )
        self.texto1.pack(pady=10, side='left')

        self.caixa1 = Entry(self.frame1)
        self.caixa1.pack(pady=10, side='right')

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.texto2 = Label(
            self.frame2,
            text='Telefone',
        )
        self.texto2.pack(pady=10, side='left')

        self.caixa2 = Entry(self.frame2)
        self.caixa2.pack(pady=10, side='right')

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.botao1 = Button(
            self.frame3,
            command=self.concatenar,
            text='Inserir',
        )
        self.botao1.pack(pady=10)

        self.frame4 = Frame(self.janela)
        self.frame4.pack()

        self.textoResultadoNome = Label(
            self.frame4,
            text='Concatenação',
            bg='black',
            fg='yellow',
        )
        self.textoResultadoNome.pack(pady=10)

        self.textoResultadoTelefone = Label(
            self.frame4,
            text='Concatenação',
            bg='black',
            fg='yellow',
        )
        self.textoResultadoTelefone.pack()

        self.janela.mainloop()


    def concatenar(self):
        self.textoResultadoNome['text'] = (f"Nome: {self.caixa1.get()}")
        self.textoResultadoTelefone['text'] = (f"Telefone: {self.caixa2.get()}")


janela = App()