import sqlite3 as db
import pickle



def adicionar_compra(table_name, filme, ticket, sala, horario):
    values_users = (str(filme), str(ticket), str(sala), str(horario))

    banco = db.connect("Usuarios.db")

    cursor = banco.cursor()

    cursor.execute(f"INSERT INTO {table_name} VALUES {values_users}")

    banco.commit()


def fazer_backup_dados(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(dados, arquivo)
        print(
            f"Backup dos dados realizado com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao fazer backup dos dados: {str(e)}")


def restaurar_backup_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            dados_restaurados = pickle.load(arquivo)
        print(f"Dados restaurados com sucesso do arquivo: {nome_arquivo}")
        return dados_restaurados
    except FileNotFoundError:
        print(f"Arquivo de backup não encontrado: {nome_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao restaurar dados do backup: {str(e)}")
        return None
