import customtkinter as ctk


class DashboardView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(
            fill="both",
            expand=True
        )

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            pady=20
        )

        descricao = ctk.CTkLabel(
            self,
            text="Bem-vindo ao WhatsApp Scheduler Pro"
        )

        descricao.pack()