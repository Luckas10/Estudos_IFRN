import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

sql.execute('CREATE TABLE teste (nome,telefone)')
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('RK','9999-9999')")
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('Maria','2222-2222')")
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('Marcos','3333-3333')")

con.commit()
con.close()
