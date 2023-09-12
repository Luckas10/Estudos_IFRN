from tkinter import *

class App:
   def __init__(self):
       self.janela = Tk()
       self.janela.title('Uso do GRID')

       self.texto1 = Label(self.janela, text='Nome: ')
       self.texto1.grid(row=0,column=0)

       self.caixa1 = Entry(self.janela)
       self.caixa1.grid(row=0,column=1,columnspan=2)

       self.botaoInserir = Button(
           self.janela,
           text='Exibir',
           command=self.exibir)
       self.botaoInserir.grid(row=1,column=1)

       self.textoResultado = Label(self.janela, text='Resultado')
       self.textoResultado['bg']='black'
       self.textoResultado['fg']='yellow'       
       self.textoResultado.grid(row=2,column=1)

       self.janela.mainloop()

   def exibir(self):
       self.textoResultado['text'] = self.caixa1.get()

aplicacao=App()
