from database.database import Database

from views.main_window import (
    MainWindow
)


def main():

    db = Database()

    db.criar_tabelas()

    app = MainWindow()

    app.mainloop()


if __name__ == "__main__":
    main()