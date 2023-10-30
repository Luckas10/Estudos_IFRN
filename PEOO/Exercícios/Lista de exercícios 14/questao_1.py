from tkinter import *
import requests, json


class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Lista 12 - Questão 01')
        self.janela.geometry("460x390")
        self.janela.resizable(width = False, height = False)

        self.Label1 = Label(background = 'white', foreground = 'black', font = 'Arial 14 bold', text = 'Consulta Informações de Pessoa Jurídica CNPJ ', )
        self.Label1.place(x = 2, y = 5, height = 43, width = 456, anchor = 'nw')
        self.Label2 = Label(font = 'Arial 14 bold', text = 'Informe CNPJ a consultar:', )
        self.Label2.place(x = 7, y = 60, height = 30, width = 236, anchor = 'nw')
        self.Entry1 = Entry(font = 'Arial 16 bold', foreground = 'blue')
        self.Entry1.place(x = 248, y = 57, height = 38, width = 201, anchor = 'nw')

        self.Button1 = Button(command=self.consultarCNPJOTO, font = 'Arial 16 bold', background = 'blue', foreground = 'white', text = 'Consultar CNPJ', )
        self.Button1.place(x = 10, y = 117, height = 37, width = 440, anchor = 'nw')

        self.Label3 = Label(anchor = 'w', text = 'Razão Social:', )
        self.Label3.place(x = 8, y = 188, height = 30, width = 101, anchor = 'nw')
        self.Label4 = Label(anchor = 'w', background = '#adadad', text = 'Razão Social resposta ', )
        self.Label4.place(x = 448, y = 186, height = 30, width = 344, anchor = 'ne')
        self.Label5 = Label(anchor = 'w', text = 'Nome Fantasia:', )
        self.Label5.place(x = 10, y = 229, height = 30, width = 113, anchor = 'nw')
        self.Label6 = Label(anchor = 'w', background = '#adadad', text = 'Nome Fantasia resposta ', )
        self.Label6.place(x = 449, y = 227, height = 30, width = 324, anchor = 'ne')
        self.Label7 = Label(anchor = 'w', text = 'Município:', )
        self.Label7.place(x = 13, y = 269, height = 30, width = 70, anchor = 'nw')
        self.Label8 = Label(anchor = 'w', background = '#adadad', text = 'Município resposta ', )
        self.Label8.place(x = 450, y = 268, height = 30, width = 358, anchor = 'ne')
        self.Label9 = Label(anchor = 'w', text = 'Estado UF :', )
        self.Label9.place(x = 12, y = 308, height = 30, width = 90, anchor = 'nw')
        self.Label10 = Label(anchor = 'w', background = '#adadad', text = 'Estado UF  resposta ', )
        self.Label10.place(x = 100, y = 309, height = 30, width = 350, anchor = 'nw')
        self.Label11 = Label(anchor = 'w', background = 'black', foreground = 'white', text = 'Situação:', )
        self.Label11.place(x = 10, y = 349, height = 30, width = 441, anchor = 'nw')

        self.janela.mainloop()


    def consultarCNPJOTO(self):
        cnpj = self.Entry1.get()
        consulta = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")

        if consulta.status_code != 200:
            self.Label11['text'] = (f"Situação: CNPJ Inválido")
        else:
            self.Label4['text'] = consulta.json()["razao_social"]
            self.Label6['text'] = consulta.json()["nome_fantasia"]
            self.Label8['text'] = consulta.json()["municipio"]
            self.Label10['text'] = consulta.json()["uf"]
            self.Label11['text'] = (f"Situação: CNPJ OK")


aplicacao=App()