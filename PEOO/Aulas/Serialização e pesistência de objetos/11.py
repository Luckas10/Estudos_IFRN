from tkinter import *
import requests, json

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("400x400")
        self.janela.title("Janelinha")

        self.canvas1 = Canvas(self.janela, width=790, height=400)
        self.canvas1.pack()

        self.Botao1 = Button(
            self.canvas1,
            width=20,
            text='Botão 1',
            bg='blue',
            fg='white',
            font='Helvetica 14',
            command=self.vercotacao,
        )
        self.Botao1.pack()

        self.textoNome2 = Label(
            self.canvas1,
            text='',
            font='Helvetica 15'
        )
        self.textoNome2.pack()

        self.janela.mainloop()

    def vercotacao(self):
        try:    
            consulta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
            cotacao = consulta.json()['USDBRL']['bid']
            self.textoNome2['text'] = (f"Cotação do dolar atual: R${cotacao}")
        except:
            self.textoNome2['text'] = (f"O seu dispositivo está sem internet")
            
    
app = App()