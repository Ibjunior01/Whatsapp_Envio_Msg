import customtkinter as ctk

from views.dashboard_view import DashboardView
from views.contato_view import ContatoView
from views.agendamento_view import AgendamentoView
from utils.theme import Theme


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.configure(
            fg_color=Theme.BACKGROUND
        )

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
            width=240,
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
        self.abrir_dashboard()
        

    def criar_menu(self):

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="WhatsApp Scheduler",
            font=("Arial", 16, "bold"),
            justify="center"
            #text_color=Theme.TEXT
        )

        titulo.pack(
            pady=20,
            padx=15,
            anchor="w"
        )

        btn_dashboard = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            command=self.abrir_dashboard
        )

        btn_dashboard.pack(
            padx=10,
            pady=5,
            fill="x"
        )

        btn_contatos = ctk.CTkButton(
            self.sidebar,
            text="Contatos",
            command=self.abrir_contatos
        )

        btn_contatos.pack(
            padx=10,
            pady=5,
            fill="x"
        )

        btn_agenda = ctk.CTkButton(
            self.sidebar,
            text="Agendamentos",
            command=self.abrir_agendamentos
        )

        btn_agenda.pack(
            padx=10,
            pady=5,
            fill="x"
        )
        
    def limpar_conteudo(self):

        for widget in self.content.winfo_children():
            widget.destroy()
            
            
# Métodos de navegação páginas
            
    def abrir_dashboard(self):

        self.limpar_conteudo()

        DashboardView(
            self.content
        )
        
    def abrir_contatos(self):

        self.limpar_conteudo()

        ContatoView(
            self.content
        )
        
    def abrir_agendamentos(self):

        self.limpar_conteudo()

        AgendamentoView(
            self.content
        )