from database.database import Database
import customtkinter as ctk
from utils.theme import Theme

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

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