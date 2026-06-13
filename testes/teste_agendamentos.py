from database.database import Database

db = Database()

conn = db.conectar()

cursor = conn.cursor()

cursor.execute(
    """
    SELECT *
    FROM agendamentos
    """
)

for item in cursor.fetchall():
    print(dict(item))

conn.close()