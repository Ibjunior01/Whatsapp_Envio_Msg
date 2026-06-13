from database.database import Database


class AgendamentoRepository:

    def __init__(self):
        self.db = Database()

    def criar(self, agendamento):

        conn = self.db.conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO agendamentos
            (
                contato_id,
                mensagem,
                data_envio,
                hora_envio
            )
            VALUES (?, ?, ?, ?)
        """,
        (
            agendamento.contato_id,
            agendamento.mensagem,
            agendamento.data_envio,
            agendamento.hora_envio
        ))

        conn.commit()
        conn.close()

    def listar(self):

        conn = self.db.conectar()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                a.id,
                c.nome,
                c.telefone,
                a.mensagem,
                a.data_envio,
                a.hora_envio,
                a.status
            FROM agendamentos a

            INNER JOIN contatos c
                ON c.id = a.contato_id

            ORDER BY
                a.data_envio,
                a.hora_envio
        """)

        agendamentos = cursor.fetchall()

        conn.close()

        return agendamentos

    
    def buscar_por_id(self, id):

        conn = self.db.conectar()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM agendamentos
            WHERE id = ?
        """, (id,))

        agendamento = cursor.fetchone()

        conn.close()

        return agendamento