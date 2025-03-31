# meu-app-api/models/livro.py
import sqlite3
from ..schemas.livro import LivroCreate

class LivroModel:
    @staticmethod
    def add_livro(livro: LivroCreate):
        """
        Adiciona um livro no banco de dados.
        """
        conn = sqlite3.connect('meu-app-api/livros.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO livros (titulo, autor, genero, resumo, status_leitura)
        VALUES (?, ?, ?, ?, ?)
        ''', (livro.titulo, livro.autor, livro.genero, livro.resumo, livro.status_leitura))

        conn.commit()
        conn.close()

    @staticmethod
    def get_livros(status=None):
        """
        Obtém todos os livros ou livros com um determinado status de leitura.
        """
        conn = sqlite3.connect('meu-app-api/livros.db')
        cursor = conn.cursor()

        if status:
            cursor.execute('SELECT * FROM livros WHERE status_leitura = ?', (status,))
        else:
            cursor.execute('SELECT * FROM livros')

        livros = cursor.fetchall()
        conn.close()

        return [{"id": livro[0], "titulo": livro[1], "autor": livro[2], "genero": livro[3], "resumo": livro[4], "status_leitura": livro[5]} for livro in livros]
