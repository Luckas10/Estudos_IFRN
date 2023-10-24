import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute("SELECT * FROM teste")

registros = sql.fetchall()

for reg in registros:
    print(reg)
