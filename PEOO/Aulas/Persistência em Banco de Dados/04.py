import sqlite3

con = sqlite3.connect("banco.db")
sql = con.cursor()

sql.execute("SELECT telefone FROM teste WHERE nome = 'Maria'")

registros = sql.fetchone()

print(registros[0])