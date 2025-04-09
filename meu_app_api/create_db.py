from meu_app_api.app import app, db
import sqlite3

def criar_tabela():
    """
    Cria a tabela 'livros' no banco de dados SQLite.
    """
    conn = sqlite3.connect('meu-app-api/livros.db')  # Conecta ou cria o banco de dados
    cursor = conn.cursor()

    # Criação da tabela 'livros', se ainda não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        genero TEXT NOT NULL,
        resumo TEXT NOT NULL,
        status_leitura TEXT NOT NULL
    );
    ''')

    # Salva as mudanças e fecha a conexão
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados e tabela criados com sucesso!")
