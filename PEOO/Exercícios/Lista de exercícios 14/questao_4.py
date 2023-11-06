import sqlite3
from tkinter import *

class App():
    import sqlite3
from tkinter import *

class App():
    def __init__(self):
        # Tela principal
        self.janela = Tk()
        self.janela.title('Lista 12 - Q4')
        self.janela.geometry('800x600')

        # Botões
        self.Button1 = Button(self.janela, text='Inserir Aluno', command=self.TelaInserirAluno, bg='blue', fg='white')
        self.Button1.pack(pady=20)

        self.Button2 = Button(self.janela, text='Excluir Aluno', command=self.TelaExcluir, bg='red', fg='white')
        self.Button2.pack(pady=20)

        self.Button3 = Button(self.janela, text='Inserir/Alterar Notas', command=self.TelaNotas, bg='green', fg='white')
        self.Button3.pack(pady=20)

        self.Button4 = Button(self.janela, text='Listar Aprovados', command=self.TelaListar, bg='purple', fg='white')
        self.Button4.pack(pady=20)

        self.frame1 = Frame(self.janela)

        self.texto1 = Label(self.frame1, text='Nota 1: ')
        self.texto1.pack(side=LEFT)

        self.caixa1 = Entry(self.frame1)
        self.caixa1.pack(side=RIGHT, pady=25)

        self.frame2 = Frame(self.janela)

        self.texto2 = Label(self.frame2, text='Nota 2: ')
        self.texto2.pack(side=LEFT)

        self.caixa2 = Entry(self.frame2)
        self.caixa2.pack(side=RIGHT, pady=25)

        self.frame3 = Frame(self.janela)

        self.texto3 = Label(self.frame3, text='Nota 3: ')
        self.texto3.pack(side=LEFT)

        self.caixa3 = Entry(self.frame3)
        self.caixa3.pack(side=RIGHT, pady=25)

        self.frame4 = Frame(self.janela)

        self.texto4 = Label(self.frame4, text='Nota 4: ')
        self.texto4.pack(side=LEFT)

        self.caixa4 = Entry(self.frame4)
        self.caixa4.pack(side=RIGHT, pady=25)

        self.frame5 = Frame(self.janela)

        self.texto5 = Label(self.frame5, text='Nome: ')
        self.texto5.pack(side=LEFT)

        self.caixa5 = Entry(self.frame5)
        self.caixa5.pack(side=RIGHT, pady=25)

        self.frame6 = Frame(self.janela)

        self.buttonInserir = Button(self.frame6, text='Inserir Aluno', command=self.InserirAluno, bg='blue', fg='white')
        self.buttonInserir.pack(pady=25)

        self.frame7 = Frame(self.janela)

        self.buttonUpdate = Button(self.frame7, text='Inserir/Alterar Notas', command=self.AlterarNotas, bg='green', fg='white')
        self.buttonUpdate.pack(pady=25)

        self.frame8 = Frame(self.janela)

        self.buttonDelete = Button(self.frame8, text='Excluir Aluno', command=self.ExcluirAluno, bg='red', fg='white')
        self.buttonDelete.pack(pady=25)

        self.frame9 = Frame(self.janela)

        self.buttonList = Button(self.frame9, text='Listar Aprovados', command=self.ListarAprovados, bg='purple', fg='white')
        self.buttonList.pack(pady=25)

        self.frame10 = Frame(self.janela)

        self.labelInfo = Label(self.frame10, text='', bg='white')
        self.labelInfo.pack(pady=25)

        self.frame11 = Frame(self.janela)

        self.buttonOk = Button(self.frame11, text='OK', command=self.OK, bg='gray', fg='white')
        self.buttonOk.pack(pady=25)


    def TelaInserirAluno(self):
        self.frame5.pack()
        self.frame6.pack()
        self.frame10.pack()
        self.frame11.pack()

        self.Button1.pack_forget()
        self.Button2.pack_forget()
        self.Button3.pack_forget()
        self.Button4.pack_forget()


    def TelaNotas(self):
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame7.pack()
        self.frame10.pack()
        self.frame11.pack()

        self.frame10.pack()

        self.Button1.pack_forget()
        self.Button2.pack_forget()
        self.Button3.pack_forget()
        self.Button4.pack_forget()


    def TelaExcluir(self):
        self.frame5.pack()
        self.frame8.pack()
        self.frame10.pack()
        self.frame11.pack()

        self.Button1.pack_forget()
        self.Button2.pack_forget()
        self.Button3.pack_forget()
        self.Button4.pack_forget()



    def TelaListar(self):
        self.frame9.pack()
        self.frame10.pack()
        self.frame11.pack()

        self.Button1.pack_forget()
        self.Button2.pack_forget()
        self.Button3.pack_forget()
        self.Button4.pack_forget()


    def OK(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame10.pack_forget()
        self.frame11.pack_forget()

        self.labelInfo.config(text='')

        self.Button1.pack(pady=20)
        self.Button2.pack(pady=20)
        self.Button3.pack(pady=20)
        self.Button4.pack(pady=20)


    #Estrutura Sqlite

    def InserirAluno(self):
        con = sqlite3.connect('bancoEscola.db')
        sql = con.cursor()

        self.nomealuno = self.caixa5.get()
        sql.execute("INSERT INTO alunos (nome, nota1, nota2, nota3, nota4) VALUES (?, NULL, NULL, NULL, NULL)", (self.nomealuno,))
        self.labelInfo.config(text='Aluno Cadastrado')
        con.commit()
        con.close()


    def AlterarNotas(self):
        con = sqlite3.connect('bancoEscola.db')
        sql = con.cursor()

        self.nomealuno = self.caixa5.get()
        self.nota1 = self.caixa1.get()
        self.nota2 = self.caixa2.get()
        self.nota3 = self.caixa3.get()        
        self.nota4 = self.caixa4.get()


        sql.execute('SELECT * FROM alunos')
        registro = sql.fetchall()

        alunoencontrado = False

        for reg in registro:
            if reg[0].strip() == self.nomealuno:
                alunoencontrado = True

        if alunoencontrado:
            sql.execute("UPDATE alunos SET nota1=?, nota2=?, nota3=?, nota4=? WHERE nome=?", 
                        (self.nota1, self.nota2, self.nota3, self.nota4, self.nomealuno))
            self.labelInfo.config(text='Notas Atualizadas')
        else:
            self.labelInfo.config(text='Aluno não encontrado')

        con.commit()
        con.close()


    def ExcluirAluno(self):
        con = sqlite3.connect('bancoEscola.db')
        sql = con.cursor()

        self.nomealuno = self.caixa5.get()

        sql.execute('SELECT * FROM alunos')
        registro = sql.fetchall()

        alunoencontrado = False

        for reg in registro:
            if reg[0].strip() == self.nomealuno:
                alunoencontrado = True

        if alunoencontrado:
            sql.execute("DELETE FROM alunos WHERE nome=?", (self.nomealuno,))
            self.labelInfo.config(text='Registro de aluno deletado')
        else:
            self.labelInfo.config(text='Aluno não encontrado')

        con.commit()
        con.close()


    def ListarAprovados(self):
        aprovados = list()

        con = sqlite3.connect('bancoEscola.db')
        sql = con.cursor()

        sql.execute('SELECT * FROM alunos')
        registros = sql.fetchall()

        cont = 0

        for reg in registros:
            nota1 = int(reg[1])
            nota2 = int(reg[2])
            nota3 = int(reg[3])
            nota4 = int(reg[4])
            nome = reg[0] + 2*'\n'
            media = (nota1 + nota2 + nota3 + nota4) / 4

            if media >= 60:
                aprovados.append(nome)
                cont += 1
            
            printar = ''

            for nome in aprovados:
                printar += nome

            if cont > 0:
                self.labelInfo.config(text=printar)
            else:
                self.labelInfo.config(text='Não há alunos aprovados')

        con.commit()
        con.close()

aplicacao = App()
aplicacao.janela.mainloop()