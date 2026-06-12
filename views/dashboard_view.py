import customtkinter as ctk

from services.dashboard_service import (
    DashboardService
)


class DashboardView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = (
            DashboardService()
        )

        self.pack(
            fill="both",
            expand=True
        )

        self.criar_componentes()

    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            pady=20
        )

        total = (
            self.service.total_contatos()
        )

        card = ctk.CTkFrame(
            self,
            width=250,
            height=120
        )

        card.pack(
            pady=20
        )

        ctk.CTkLabel(
            card,
            text="Total de Contatos",
            font=("Arial", 16)
        ).pack(
            pady=(20, 5)
        )

        ctk.CTkLabel(
            card,
            text=str(total),
            font=("Arial", 30, "bold")
        ).pack()