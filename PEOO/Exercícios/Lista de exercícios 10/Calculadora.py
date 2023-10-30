from tkinter import *

class App:
    def __init__(self) -> None:
        self.janela = Tk()
        self.janela.title("Calculadora 01")
        self.janela.geometry('250x200')

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.texto1 = Label(
            self.frame1,
            text='Valor 1 : ',
        )
        self.texto1.pack(pady=10, side='left')

        self.caixaValor1 = Entry(self.frame1)
        self.caixaValor1.pack(pady=10, side='right')

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.texto2 = Label(
            self.frame2,
            text='Valor 2 : ',
        )
        self.texto2.pack(pady=10, side='left')

        self.caixaValor2 = Entry(self.frame2)
        self.caixaValor2.pack(pady=10, side='right')

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.botaoSoma = Button(
            self.frame3,
            command=self.Somar,
            width=3,
            text='+',
        )
        self.botaoSoma.pack(side='left')

        self.botaoSubtrair = Button(
            self.frame3,
            command=self.Subtrair,
            width=3,
            text='-',
        )
        self.botaoSubtrair.pack(side='left')

        self.botaoMultiplicar = Button(
            self.frame3,
            command=self.Multiplicar,
            width=3,
            text='*',
        )
        self.botaoMultiplicar.pack(side='left')

        self.botaoDividir = Button(
            self.frame3,
            command=self.Dividir,
            width=3,
            text='/',
        )
        self.botaoDividir.pack(side='left')

        self.frame4 = Frame(self.janela)
        self.frame4.pack()

        self.textoIgual = Label(
            self.frame4,
            text=' = ',
        )
        self.textoIgual.pack(side='left', pady=10)

        self.textoResultado = Label(
            self.frame4,
            text='                     ',
        )
        self.textoResultado.pack(side='left', pady=10)
        
        self.frame5 = Frame(self.janela)
        self.frame5.pack()

        self.botaoLimpar = Button(
            self.frame5,
            command=self.Limpar,
            text='Limpar',
        )
        self.botaoLimpar.pack(side='left')

        self.botaoSair = Button(
            self.frame5,
            command=self.Sair,
            text='Sair',
        )
        self.botaoSair.pack(side='left')
        
        self.janela.mainloop()


    def Somar(self):
        resultado = int(self.caixaValor1.get()) + int(self.caixaValor2.get())
        self.textoResultado['text'] = (f"Resultado: {resultado}")


    def Subtrair(self):
        resultado = int(self.caixaValor1.get()) - int(self.caixaValor2.get())
        self.textoResultado['text'] = (f"Resultado: {resultado}")


    def Multiplicar(self):
        resultado = int(self.caixaValor1.get()) * int(self.caixaValor2.get())
        self.textoResultado['text'] = (f"Resultado: {resultado}")


    def Dividir(self):
        resultado = int(self.caixaValor1.get()) / int(self.caixaValor2.get())
        self.textoResultado['text'] = (f"Resultado: {resultado}")

    
    def Limpar(self):
        self.caixaValor1.delete(0, END)
        self.caixaValor2.delete(0, END)
        self.textoResultado['text'] = '                     '


    def Sair(self):
        exit()


def main():
    janela = App()


if __name__ == "__main__":
    main()
