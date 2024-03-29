import sqlite3 as db


def criar_banco(name_db):
    banco = db.connect(f"{name_db}.db")


def criar_tabela(table_name, name_db):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(f"CREATE TABLE {table_name} (nome text, acompanhantes integer, email text)")

    banco.commit()


def adicionar_user(table_name, name_db, values_users=()):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(f"INSERT INTO {table_name} VALUES {values_users}")

    banco.commit()


def listar_usuarios(table_name, name_db):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")

    lista = cursor.fetchall()

    return lista


def search_info_gerais(filme):
    banco = db.connect("Admin.db")

    cursor = banco.cursor()

    cursor.execute(f"SELECT * FROM Info_gerais")

    valores = cursor.fetchall()

    dados_filme = {}

    for tupla in valores:
        if tupla[0] == filme:
            dados_filme["sala"] = tupla[1]
            dados_filme["horario"] = tupla[2]

    return dados_filme


def search_tickets(user, ticket_informado):
    verificador = False

    banco = db.connect("Usuarios.db")

    cursor = banco.cursor()

    cursor.execute(f"SELECT * FROM {user}")

    valores = cursor.fetchall()

    dados_filme = {}

    for tupla in valores:
        if tupla[1] == ticket_informado:
            dados_filme["filme"] = tupla[0]
            dados_filme["sala"] = tupla[2]
            dados_filme["horario"] = tupla[3]
            verificador = True

    if verificador == True:
        return dados_filme
    else:
        return verificador


def criar_tabela_user(table_name, name_db):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(
        f"CREATE TABLE {table_name} (filme text, ticket text, sala text, horario text)")

    banco.commit()


def deletar_compra(ticket_informado, user):
    try:

        banco_admin = db.connect("Admin.db")
        banco_users = db.connect("Usuarios.db")

        cursor_admin = banco_admin.cursor()
        cursor_users = banco_users.cursor()

        cursor_admin.execute(
            "DELETE FROM Tickets WHERE ticket = ?", (str(ticket_informado),))
        cursor_users.execute(
            f"DELETE FROM {user} WHERE ticket = ?", (str(ticket_informado),))

        banco_admin.commit()
        banco_admin.close()

        banco_users.commit()
        banco_users.close()

        print("Os dados foram removidos com sucesso!")

    except db.Error as erro:
        print(f"Erro ao excluir: {erro}")


adicionar_user("Inscricoes", "Eventos", ("João Lucas", 1, "johndescraft1@gmail.com"))