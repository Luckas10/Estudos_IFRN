from tkinter import *

class App:
   def __init__(self):
       self.janela = Tk()
       self.janela.title('Uso do PLACE')
       self.janela.geometry('280x200')

       self.label1 = Label(self.janela, text = "Nota 1")
       self.label1.place(x = 10,y = 10)

       self.entrada1 = Entry(self.janela, bd = 5)
       self.entrada1.place(x = 60,y = 10)

       self.label2 = Label(self.janela,text = "Nota 2")
       self.label2.place(x = 10,y = 50)

       self.entrada2 = Entry(self.janela,bd = 5)
       self.entrada2.place(x = 60,y = 50)
       self.label3 = Label(self.janela,text = "Soma =")
       self.label3.place(x = 10,y = 150)

       self.resultado = Label(self.janela,text='Resultado')
       self.resultado.place(x = 70,y = 150)

       self.botao = Button(self.janela, text = "Calcular",command=self.calcular)
       self.botao.place(x = 100, y = 100)

       self.janela.mainloop()

   def calcular(self):
       self.resultado['text'] = float(self.entrada1.get())+float(self.entrada2.get())
  
aplicacao=App()
