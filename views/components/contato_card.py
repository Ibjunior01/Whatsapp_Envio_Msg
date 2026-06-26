import customtkinter as ctk
from utils.theme import Theme
from services.contato_service import (ContatoService)


class ContatoCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        contato_id,
        nome,
        telefone,
        refresh_callback
    ):
        super().__init__(
            master,
            fg_color=Theme.SURFACE,
            corner_radius=12,
            border_width=1,
            border_color=Theme.BORDER
        )

        self.pack(
            fill="x",
            padx=10,
            pady=8
        )

        ctk.CTkLabel(
            self,
            text=f"#{contato_id}",
            text_color=Theme.SECONDARY,
            font=("Arial", 12, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 0)
        )

        ctk.CTkLabel(
            self,
            text=nome,
            text_color=Theme.TEXT,
            font=("Arial", 15, "bold")
        ).pack(
            anchor="w",
            padx=15
        )

        ctk.CTkLabel(
            self,
            text=telefone,
            text_color=Theme.TEXT_MUTED
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 10)
        )
        
        
        ctk.CTkButton(
            self,
            text="Excluir",
            fg_color=Theme.ERROR,
            hover_color="#B91C1C",
            width=90,
            command=self.excluir
        ).pack(
            pady=(0, 10)
        )
        
        
        def excluir(self):

            service = ContatoService()

            service.excluir_contato(
                self.contato_id
            )

            self.refresh_callback()
        
        
        self.contato_id = contato_id
        self.refresh_callback = refresh_callback