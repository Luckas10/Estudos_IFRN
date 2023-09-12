from tkinter import *

class App:
  def __init__(self):
       self.janela = Tk()
     
       self.texto1 = Label(self.janela,text='texto1')
       self.texto1.grid(row=0,column=0)

       self.texto2 = Label(self.janela,text='texto2')
       self.texto2.grid(row=1,column=1)

       self.texto3 = Label(self.janela,text='texto3')
       self.texto3.grid(row=2,column=2)

    

       self.janela.mainloop()

aplicacao=App()
