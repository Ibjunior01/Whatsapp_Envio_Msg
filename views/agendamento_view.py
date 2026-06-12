import customtkinter as ctk


class AgendamentoView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(
            fill="both",
            expand=True
        )

        titulo = ctk.CTkLabel(
            self,
            text="Agendamentos",
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            pady=20
        )

        descricao = ctk.CTkLabel(
            self,
            text="Módulo de agendamentos em construção"
        )

        descricao.pack()