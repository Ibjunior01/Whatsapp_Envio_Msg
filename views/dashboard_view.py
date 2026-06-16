import customtkinter as ctk

from services.dashboard_service import (
    DashboardService
)

from views.components.dashboard_card import (
    DashboardCard
)

from utils.theme import Theme


class DashboardView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.service = DashboardService()

        self.configure(
            fg_color=Theme.BACKGROUND
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
            font=("Arial", 28, "bold"),
            text_color=Theme.TEXT
        )

        titulo.pack(
            pady=(20, 30)
        )

        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards_frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=20
        )
        
        cards_frame.grid_columnconfigure(
            0,
            weight=1
        )

        cards_frame.grid_columnconfigure(
            1,
            weight=1
        )

        # Grid 2x2
        DashboardCard(
            cards_frame,
            "👥 Contatos",
            self.service.total_contatos()
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=15
        )

        DashboardCard(
            cards_frame,
            "📅 Agendamentos",
            self.service.total_agendamentos()
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=15
        )

        DashboardCard(
            cards_frame,
            "⏳ Pendentes",
            self.service.total_pendentes()
        ).grid(
            row=1,
            column=0,
            padx=15,
            pady=15
        )

        DashboardCard(
            cards_frame,
            "✅ Enviados",
            self.service.total_enviados()
        ).grid(
            row=1,
            column=1,
            padx=15,
            pady=15
        )