from database.database import Database
from models.contato import Contato
from typing import List


class ContatoRepository:

    def __init__(self):
        self.db = Database()

# Inserir contato
    def criar(self, contato):

        conn = self.db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO contatos
            (
                nome,
                telefone,
                empresa,
                observacoes
            )
            VALUES (?, ?, ?, ?)
        """,
        (
            contato.nome,
            contato.telefone,
            contato.empresa,
            contato.observacoes
        ))

        conn.commit()
        conn.close()

# Listar todos
    def listar(self) -> List:

        conn = self.db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM contatos
            ORDER BY nome
        """)

        contatos = cursor.fetchall()

        conn.close()

        return contatos
    
# Buscar por Id
    def buscar_por_id(self, id):

        conn = self.db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM contatos
            WHERE id = ?
        """, (id,))

        contato = cursor.fetchone()

        conn.close()

        return contato

# Atualizar
    def atualizar(self, contato):

        conn = self.db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE contatos
            SET
                nome = ?,
                telefone = ?,
                empresa = ?,
                observacoes = ?
            WHERE id = ?
        """,
        (
            contato.nome,
            contato.telefone,
            contato.empresa,
            contato.observacoes,
            contato.id
        ))

        conn.commit()
        conn.close()

# Excluir
    def excluir(self, id):

        conn = self.db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM contatos
            WHERE id = ?
        """, (id,))

        conn.commit()
        conn.close()