import customtkinter as ctk

from services.contato_service import (
    ContatoService
)

from utils.messages import Messages
from utils.theme import Theme

from views.components.contato_card import (
    ContatoCard
)


class ContatoView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = ContatoService()

        self.configure(
            fg_color=Theme.BACKGROUND
        )

        self.pack(
            fill="both",
            expand=True
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_columnconfigure(
            1,
            weight=2
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.criar_layout()

    def criar_layout(self):

        # ESQUERDA

        self.form_frame = ctk.CTkFrame(
            self,
            fg_color=Theme.SURFACE
        )

        self.form_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=15,
            pady=15
        )

        # DIREITA

        self.list_frame = ctk.CTkFrame(
            self,
            fg_color=Theme.BACKGROUND
        )

        self.list_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(0, 15),
            pady=15
        )

        self.criar_formulario()
        self.criar_lista()

    def criar_formulario(self):

        ctk.CTkLabel(
            self.form_frame,
            text="Novo Contato",
            font=("Arial", 18, "bold"),
            text_color=Theme.TEXT
        ).pack(
            pady=15
        )

        ctk.CTkLabel(
            self.form_frame,
            text="Nome",
            text_color=Theme.TEXT,
            font=("Arial", 12, "bold")
        ).pack(
            pady=(10, 5),
            
        )

        self.nome_entry = ctk.CTkEntry(
            self.form_frame,
            width=320,
            placeholder_text="Digite o nome"
        )

        self.nome_entry.pack(
            pady=(0, 10)
        )

        ctk.CTkLabel(
            self.form_frame,
            text="Telefone",
            text_color=Theme.TEXT,
            font=("Arial", 12, "bold")
        ).pack(
            pady=(10, 5)
        )

        self.telefone_entry = ctk.CTkEntry(
            self.form_frame,
            width=320,
            placeholder_text="(85) 99999-0000"
        )

        self.telefone_entry.pack(
            pady=(0, 15)
        )
        

        ctk.CTkButton(
            self.form_frame,
            text="Salvar",
            fg_color=Theme.PRIMARY,
            command=self.salvar
        ).pack(
            pady=10
        )

    def criar_lista(self):

        ctk.CTkLabel(
            self.list_frame,
            text="Contatos",
            font=("Arial", 18, "bold"),
            text_color=Theme.TEXT
        ).pack(
            pady=10
        )

        self.scroll = ctk.CTkScrollableFrame(
            self.list_frame,
            fg_color="transparent"
        )

        self.scroll.pack(
            fill="both",
            expand=True
        )

        self.carregar_contatos()

    def carregar_contatos(self):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        contatos = (
            self.service.listar_contatos()
        )

        for contato in contatos:

            ContatoCard(
            self.scroll,
            contato_id=contato["id"],
            nome=contato["nome"],
            telefone=contato["telefone"],
            refresh_callback=self.carregar_contatos
        )

    def salvar(self):

        nome = self.nome_entry.get()

        telefone = (
            self.telefone_entry.get()
        )

        if not nome.strip():

            Messages.aviso(
                "Informe o nome."
            )

            return

        if not telefone.strip():

            Messages.aviso(
                "Informe o telefone."
            )

            return

        self.service.criar_contato(
            nome,
            telefone
        )

        self.carregar_contatos()

        self.nome_entry.delete(
            0,
            "end"
        )

        self.telefone_entry.delete(
            0,
            "end"
        )

        Messages.sucesso(
            "Contato salvo com sucesso."
        )