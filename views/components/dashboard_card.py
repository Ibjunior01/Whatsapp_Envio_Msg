import customtkinter as ctk
from utils.theme import Theme


class DashboardCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        titulo,
        valor
    ):
        super().__init__(
            master,
            width=280,
            height=160,
            fg_color=Theme.SURFACE,
            corner_radius=15,
            border_width=1,
            border_color=Theme.BORDER
        )

        self.pack_propagate(False)
        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text=titulo,
            font=("Arial", 16),
            text_color=Theme.TEXT_MUTED
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            self,
            text=str(valor),
            font=("Arial", 42, "bold"),
            text_color=Theme.TEXT
        ).pack(
            expand=True
        )