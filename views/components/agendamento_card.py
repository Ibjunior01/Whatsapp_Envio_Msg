import customtkinter as ctk
from utils.theme import Theme
from services.whatsapp_service import WhatsAppService
from datetime import datetime


class AgendamentoCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        nome,
        telefone,
        mensagem,
        data_hora,
        status
    ):
        super().__init__(
            master,
            fg_color=Theme.SURFACE,
            corner_radius=12,
            border_width=1,
            border_color=Theme.BORDER
        )

        self.whatsapp_service = WhatsAppService()

        self.telefone = telefone
        self.mensagem = mensagem
        self.status = status
        self.master = master

        self.pack(
            fill="x",
            padx=10,
            pady=8
        )

        # --- UI ---
        ctk.CTkLabel(
            self,
            text=nome,
            font=("Arial", 15, "bold"),
            text_color=Theme.TEXT
        ).pack(anchor="w", padx=15, pady=(10, 2))

        ctk.CTkLabel(
            self,
            text=telefone,
            text_color=Theme.TEXT_MUTED
        ).pack(anchor="w", padx=15)

        ctk.CTkLabel(
            self,
            text=mensagem,
            text_color=Theme.TEXT,
            wraplength=600,
            justify="left"
        ).pack(anchor="w", padx=15, pady=(5, 0))

        footer = ctk.CTkFrame(self, fg_color="transparent")
        footer.pack(fill="x", padx=15, pady=10)

        try:

            data_formatada = datetime.strptime(
                data_hora,
                "%Y-%m-%d %H:%M"
            ).strftime(
                "%d/%m/%Y %H:%M"
            )

        except:

            data_formatada = data_hora


        ctk.CTkLabel(
            footer,
            text=f"📅 {data_formatada}",
            text_color=Theme.TEXT_MUTED
        ).pack(side="left")

        status_color = {
            "PENDENTE": Theme.SECONDARY,
            "ENVIADO": Theme.SUCCESS,
            "FALHA": Theme.ERROR
        }.get(status, Theme.TEXT_MUTED)

        self.status_label = ctk.CTkLabel(
            footer,
            text=status,
            text_color=status_color,
            font=("Arial", 12, "bold")
        )
        self.status_label.pack(side="right")

        # BOTÃO
        ctk.CTkButton(
            self,
            text="Enviar Agora",
            fg_color="#10B981",
            hover_color="#059669",
            command=self.enviar_agora
        ).pack(anchor="e", padx=15, pady=(0, 10))
        
    
    
    
    def enviar_agora(self):

        sucesso = self.whatsapp_service.enviar_mensagem(
            self.telefone,
            self.mensagem
        )

        if sucesso:
            self.status = "ENVIADO"
            self.status_label.configure(
                text="ENVIADO",
                text_color=Theme.SUCCESS
            )
            print("Mensagem enviada com sucesso!")

        else:
            self.status_label.configure(
                text="FALHA",
                text_color=Theme.ERROR
            )
            print("Falha ao enviar mensagem")