import customtkinter as ctk

from views.contato_view import ContatoView


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(
            "WhatsApp Scheduler Pro"
        )

        self.geometry(
            "1200x700"
        )

        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.criar_layout()

    def criar_layout(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.content = ctk.CTkFrame(
            self
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.criar_menu()

        ContatoView(
            self.content
        )

    def criar_menu(self):

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="WhatsApp Scheduler",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=20
        )

        btn_dashboard = ctk.CTkButton(
            self.sidebar,
            text="Dashboard"
        )

        btn_dashboard.pack(
            padx=10,
            pady=5,
            fill="x"
        )

        btn_contatos = ctk.CTkButton(
            self.sidebar,
            text="Contatos"
        )

        btn_contatos.pack(
            padx=10,
            pady=5,
            fill="x"
        )

        btn_agenda = ctk.CTkButton(
            self.sidebar,
            text="Agendamentos"
        )

        btn_agenda.pack(
            padx=10,
            pady=5,
            fill="x"
        )