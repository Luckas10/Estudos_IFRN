import sqlite3

conexaoSql = sqlite3.connect('alunos.db')
sql = conexaoSql.cursor()

sql.execute('CREATE TABLE registros (matricula,nome)')
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('RK','9999-9999')")
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('Maria','2222-2222')")
sql.execute("INSERT INTO teste (nome,telefone) VALUES ('Marcos','3333-3333')")

conexaoSql.commit()
conexaoSql.close()
