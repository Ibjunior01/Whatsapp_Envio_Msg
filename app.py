from database.database import Database


def main():
    db = Database()

    db.criar_tabelas()

    print(
        "Banco criado com sucesso!"
    )

if __name__ == "__main__":
    main()