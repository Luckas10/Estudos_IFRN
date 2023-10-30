from tkinter import *
import requests, json


class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Lista 12 - Questão 03')
        self.janela.geometry('580x290')
        self.janela.resizable(width = False, height = False)

        self.Label1 = Label(background = 'green', font = 'Arial 16 bold', foreground = 'yellow', text = 'Consulta disponibilidade de domínio Internet .BR ')
        self.Label1.place(x = 1, y = 1, height = 52, width = 575, anchor = 'nw')
        self.Label2 = Label(font = 'Arial 14 bold', text = 'Insira o domínio .BR que deseja consultar disponibilidade:')
        self.Label2.place(x = 11, y = 59, height = 30, width = 556, anchor = 'nw')
        self.Entry1 = Entry(font = 'Arial 14 bold', foreground = 'blue', justify = 'center')
        self.Entry1.place(x = 3, y = 92, height = 35, width = 573, anchor = 'nw')
        self.Button1 = Button(command=self.consultarSITE, font = 'Arial 14 bold', text = 'Consultar Disponibilidade', )
        self.Button1.place(x = 142, y = 147, height = 48, width = 301, anchor = 'nw')
        self.LabelFrame1 = LabelFrame(text = 'Situação do Domínio Consultado')
        self.LabelFrame1.place(x = 9, y = 205, height = 81, width = 565,anchor = 'nw')
        self.Label3 = Label(background = 'gray', font = 'Arial 16 bold', text = 'Aguardando Consulta')
        self.Label3.place(x = 31, y = 231, height = 38, width = 527, anchor = 'nw')

        self.janela.mainloop()


    def consultarSITE(self):
        dominio = self.Entry1.get()
        consulta = requests.get(f"https://brasilapi.com.br/api/registrobr/v1/{dominio}")

        if consulta.json()['status'] == "REGISTERED":
            self.Label3['text'] = "Domínio NÃO Disponível"
        else:
            self.Label3['text'] = "Domínio Disponível"


aplicacao=App()