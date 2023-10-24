import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute("DELETE FROM teste WHERE nome = 'Maria'")

con.commit()
con.close()
