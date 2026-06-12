import sqlite3

from pathlib import Path

class Database:
    def __init__(self):
        self.db_path = Path("data/banco.db")

        self.db_path.parent.mkdir(
            exist_ok=True
        )
    
    def conectar(self):

        conn = sqlite3.connect(
            self.db_path
        )

        conn.row_factory = sqlite3.Row

        return conn

    def criar_tabelas(self):
        conn = self.conectar()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,         
            telefone TEXT NOT NULL UNIQUE,
            empresa TEXT,
            observacoes TEXT,
            
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contato_id INTEGER NOT NULL,
            mensagem TEXT NOT NULL,
            data_envio TEXT NOT NULL,
            hora_envio TEXT NOT NULL,
            status TEXT DEFAULT 'PENDENTE',
            
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(contato_id)
            REFERENCES contatos(id)
)
""")
        
        
        
        
        
        conn.commit()
        conn.close()