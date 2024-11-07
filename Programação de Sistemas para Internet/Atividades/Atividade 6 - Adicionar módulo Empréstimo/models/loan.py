from database import get_connection
from datetime import datetime, timedelta

class Loan:
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=14)

    def save(self):
        conn = get_connection()
        conn.execute(
            "INSERT INTO loans(user_id, book_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
            (self.user_id, self.book_id, self.data_emprestimo, self.data_devolucao)
        )
        conn.execute(
            "UPDATE books SET disponivel = 0 WHERE id = ?", (self.book_id,)
        )
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        loans = conn.execute("""
            SELECT loans.id AS loan_id, books.id AS book_id, books.titulo, users.nome, loans.data_emprestimo, loans.data_devolucao 
            FROM loans 
            JOIN books ON loans.book_id = books.id 
            JOIN users ON loans.user_id = users.id
        """).fetchall()
        conn.close()
        return [dict(loan) for loan in loans]


    @classmethod
    def return_book(cls, loan_id, book_id):
        conn = get_connection()
        conn.execute("DELETE FROM loans WHERE id = ?", (loan_id,))
        conn.execute("UPDATE books SET disponivel = 1 WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
