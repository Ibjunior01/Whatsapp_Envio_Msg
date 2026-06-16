# from repositories.contato_repository import ContatoRepository

# repo = ContatoRepository()

# repo.excluir(3)

# print("Contato removido!")

from database.database import Database

db = Database()

conn = db.conectar()

cursor = conn.cursor()

cursor.execute("""
DELETE FROM agendamentos
WHERE data_envio LIKE '%/%'
""")

conn.commit()

print("Removidos:", cursor.rowcount)



conn.close()