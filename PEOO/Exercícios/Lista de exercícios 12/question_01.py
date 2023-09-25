from tkinter import *

class App:
    def __init__(self):
        self.temp = "0"
        self.listaValores = []
        self.operacao = ""
        self.resultado = 0

        self.janela = Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("320x280")

        self.canvas1 = Canvas(self.janela)
        self.canvas1.configure(
            bg='gray',
            width=320,
            height=280,
        )
        self.canvas1.pack()

        self.logoIFRN = PhotoImage(file="logo_ifrn_01.png").subsample(13, 13)

        self.imagemExibida = self.canvas1.create_image(52, 57.3, image=self.logoIFRN)

        self.canvas1.tag_bind(self.imagemExibida, "<Button-1>", self.mudaCor)

        self.textoLista12 = self.canvas1.create_text(265, 260, text="Lista 12", font=("Arial", 15), fill="white")

        self.label1 = Label(
            self.canvas1,
            text="0.00",
            font=("Arial", 18),
            justify=RIGHT,
            anchor=E,
            height=3,
            width=14,
            bg="white",
        )
        self.label1.place(x=100.5, y=15)

        self.botao0 = Button(
            self.canvas1,
            text="0",
            height=1,
            width=6,
            command=self.Numero0,
        )
        self.botao0.place(x=23.7, y=212.1)

        self.botao1 = Button(
            self.canvas1,
            text="1",
            height=1,
            width=6,
            command=self.Numero1,
        )
        self.botao1.place(x=23.7, y=180.2)

        self.botao2 = Button(
            self.canvas1,
            text="2",
            height=1,
            width=6,
            command=self.Numero2,
        )
        self.botao2.place(x=80.3, y=180.2)

        self.botao3 = Button(
            self.canvas1,
            text="3",
            height=1,
            width=6,
            command=self.Numero3,
        )
        self.botao3.place(x=136.4, y=180.2)

        self.botao4 = Button(
            self.canvas1,
            text="4",
            height=1,
            width=6,
            command=self.Numero4,
        )
        self.botao4.place(x=23.7, y=148.4)

        self.botao5 = Button(
            self.canvas1,
            text="5",
            height=1,
            width=6,
            command=self.Numero5,
        )
        self.botao5.place(x=80.3, y=148.4)

        self.botao6 = Button(
            self.canvas1,
            text="6",
            height=1,
            width=6,
            command=self.Numero6,
        )
        self.botao6.place(x=136.4, y=148.4)

        self.botao7 = Button(
            self.canvas1,
            text="7",
            height=1,
            width=6,
            command=self.Numero7,
        )
        self.botao7.place(x=23.7, y=116.3)

        self.botao8 = Button(
            self.canvas1,
            text="8",
            height=1,
            width=6,
            command=self.Numero8,
        )
        self.botao8.place(x=80.3, y=116.3)

        self.botao9 = Button(
            self.canvas1,
            text="9",
            height=1,
            width=6,
            command=self.Numero9,
        )
        self.botao9.place(x=136.4, y=116.3)
        
        self.botaoPonto = Button(
            self.canvas1,
            text=".",
            height=1,
            width=6,
        )
        self.botaoPonto.place(x=80.3, y=212.1)

        self.botaoC = Button(
            self.canvas1,
            text="C",
            bg="yellow",
            height=1,
            width=6,
            command=self.ApagarTudo,
        )
        self.botaoC.place(x=136.4, y=212.1)

        self.botaoSomar = Button(
            self.canvas1,
            bg="white",
            text="+",
            height=1,
            width=6,
            command=self.Somar,
        )
        self.botaoSomar.place(x=193, y=116.3)

        self.botaoSubtrair = Button(
            self.canvas1,
            bg="white",
            text="-",
            height=1,
            width=6,
            command=self.Subtrair,
        )
        self.botaoSubtrair.place(x=193, y=148.4)

        self.botaoDividir = Button(
            self.canvas1,
            bg="white",
            text="/",
            height=1,
            width=6,
            command=self.Dividir,
        )
        self.botaoDividir.place(x=193, y=180.2)

        self.botaoMultiplicar = Button(
            self.canvas1,
            bg="white",
            text="*",
            height=1,
            width=6,
            command=self.Multiplicar,
        )
        self.botaoMultiplicar.place(x=193, y=212.1)

        self.botaoBackSpace = Button(
            self.canvas1,
            text="←",
            bg="red",
            height=1,
            width=6,
            command=self.BackSpace,
        )
        self.botaoBackSpace.place(x=249.2, y=116.3)

        self.botaoResultado = Button(
            self.canvas1,
            bg="black",
            fg="white",
            text="=",
            height=5,
            width=6,
            command=self.Resultado,
        )
        self.botaoResultado.place(x=249.2, y=150)

        self.janela.mainloop()

    
    def mudaCor(self, evento):
        if self.botaoResultado["bg"] == "black":
            self.botaoResultado["bg"] = "blue"
        else:
            self.botaoResultado["bg"] = "black"


    def Numero0(self):
        self.temp += "0"
        self.label1["text"] = self.temp
    def Numero1(self):
        self.temp += "1"
        self.label1["text"] = self.temp
    def Numero2(self):
        self.temp += "2"
        self.label1["text"] = self.temp
    def Numero3(self):
        self.temp += "3"
        self.label1["text"] = self.temp
    def Numero4(self):
        self.temp += "4"
        self.label1["text"] = self.temp
    def Numero5(self):
        self.temp += "5"
        self.label1["text"] = self.temp
    def Numero6(self):
        self.temp += "6"
        self.label1["text"] = self.temp
    def Numero7(self):
        self.temp += "7"
        self.label1["text"] = self.temp
    def Numero8(self):
        self.temp += "8"
        self.label1["text"] = self.temp
    def Numero9(self):
        self.temp += "9"
        self.label1["text"] = self.temp


    def Somar(self):
        self.listaValores.append(float(self.temp))
        self.temp = "0"
        self.operacao = "+"
        self.label1["text"] = self.temp

    
    def Subtrair(self):
        self.listaValores.append(float(self.temp))
        self.temp = "0"
        self.operacao = "-"
        self.label1["text"] = self.temp


    def Multiplicar(self):
        self.listaValores.append(float(self.temp))
        self.temp = "0"
        self.operacao = "*"
        self.label1["text"] = self.temp


    def Dividir(self):
        self.listaValores.append(float(self.temp))
        self.temp = "0"
        self.operacao = "/"
        self.label1["text"] = self.temp


    def Resultado(self):
        if self.operacao == "+":
            self.listaValores.append(float(self.temp))
            self.resultado += sum(self.listaValores)
            self.label1["text"] = self.resultado
            self.listaValores = [0]
            self.temp = "0"

        elif self.operacao == "-":
            self.listaValores.append(float(self.temp))
            for k, i in enumerate(self.listaValores):
                if k == 0:
                    self.resultado += i
                else:
                    self.resultado -= i
            self.label1["text"] = self.resultado
            self.listaValores = [0]
            self.temp = "0"

        elif self.operacao == "*":
            self.listaValores.append(float(self.temp))
            for k, i in enumerate(self.listaValores):
                if k == 0:
                    self.resultado += i
                else:
                    self.resultado *= i
            self.label1["text"] = self.resultado
            self.listaValores = [0]
            self.temp = "0"

        elif self.operacao == "/":
            try:
                self.listaValores.append(float(self.temp))
                for k, i in enumerate(self.listaValores):
                    if k == 0:
                        self.resultado += i
                    else:
                        self.resultado /= i
                self.label1["text"] = self.resultado
                self.listaValores = [0]
                self.temp = "0"
            except ZeroDivisionError:
                self.label1["text"] = "Não / por 0"
    

    def ApagarTudo(self):
        self.temp = "0"
        self.label1["text"] = self.temp
        self.resultado = 0
        self.listaValores = []
        self.operacao = ""


    def BackSpace(self):
        self.temp2 = self.label1.cget('text') 
        self.temp2 = str(self.temp2)
        if self.temp2 != '0':
            self.temp = self.temp2[:-1]
            self.label1.config(text=self.temp)
            if len(self.temp) == 1:
                self.label1.config(text='0')


calculadora = App()
