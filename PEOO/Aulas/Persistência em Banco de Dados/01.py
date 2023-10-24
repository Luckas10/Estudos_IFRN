import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute('CREATE TABLE teste (nome,telefone)')
