import customtkinter as ctk

from services.contato_service import ContatoService
from services.agendamento_service import AgendamentoService
from views.components.agendamento_card import AgendamentoCard
from utils.theme import Theme


class AgendamentoView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.contato_service = ContatoService()
        self.agendamento_service = AgendamentoService()

        self.configure(fg_color=Theme.BACKGROUND)

        self.pack(fill="both", expand=True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self.criar_layout()
        
    
    def criar_layout(self):

        # LEFT (FORM)
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

        # RIGHT (LIST)
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
            text="Novo Agendamento",
            font=("Arial", 18, "bold"),
            text_color=Theme.TEXT
        ).pack(pady=15)

        # CONTATO
        ctk.CTkLabel(
            self.form_frame,
            text="Contato"
        ).pack(anchor="w", padx=10)

        contatos = self.contato_service.listar_contatos()
        self.contatos_map = {c["nome"]: c["id"] for c in contatos}

        self.contato_combo = ctk.CTkComboBox(
            self.form_frame,
            values=list(self.contatos_map.keys()),
            width=250
        )
        self.contato_combo.pack(pady=(0, 10))

        # MENSAGEM
        ctk.CTkLabel(
            self.form_frame,
            text="Mensagem"
        ).pack(anchor="w", padx=10)

        self.mensagem_entry = ctk.CTkTextbox(
            self.form_frame,
            width=300,
            height=120
            
        )
        self.mensagem_entry.pack(pady=(0, 10))

        # DATA
        ctk.CTkLabel(
            self.form_frame,
            text="Data (YYYY-MM-DD)"
        ).pack(anchor="w", padx=10)

        self.data_entry = ctk.CTkEntry(
            self.form_frame,
            width=250,
            placeholder_text="20-06-2026"
        )
        self.data_entry.pack(pady=(0, 10))

        # HORA
        ctk.CTkLabel(
            self.form_frame,
            text="Hora (HH:MM)"
        ).pack(anchor="w", padx=10)

        self.hora_entry = ctk.CTkEntry(
            self.form_frame,
            width=250,
            placeholder_text="09:00"
        )
        self.hora_entry.pack(pady=(0, 15))

        # BOTÃO
        ctk.CTkButton(
            self.form_frame,
            text="Agendar",
            fg_color=Theme.PRIMARY,
            command=self.agendar
        ).pack(pady=10)
    

    def criar_lista(self):

        ctk.CTkLabel(
            self.list_frame,
            text="Agendamentos",
            font=("Arial", 18, "bold"),
            text_color=Theme.TEXT
        ).pack(pady=10)

        self.scroll = ctk.CTkScrollableFrame(
            self.list_frame,
            fg_color="transparent"
        )
        self.scroll.pack(fill="both", expand=True)

        self.carregar_agendamentos()


    def carregar_agendamentos(self):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        agendamentos = self.agendamento_service.listar_agendamentos()

        for a in agendamentos:

            data_hora = f"{a['data_envio']} {a['hora_envio']}"

            AgendamentoCard(
                self.scroll,
                nome=a["nome"],
                telefone=a["telefone"],
                mensagem=a["mensagem"],
                data_hora=data_hora,
                status=a["status"]
            )
            
    
    def agendar(self):

        nome = self.contato_combo.get()
        contato_id = self.contatos_map[nome]

        mensagem = self.mensagem_entry.get("1.0", "end").strip()
        data_envio = self.data_entry.get()
        hora_envio = self.hora_entry.get()

        self.agendamento_service.criar_agendamento(
            contato_id,
            mensagem,
            data_envio,
            hora_envio
        )

        self.carregar_agendamentos()

        print("Agendamento salvo!")


    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Agendamentos",
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            pady=(20, 10)
        )

        formulario = ctk.CTkFrame(
            self
        )

        formulario.pack(
            padx=20,
            pady=20,
            fill="x"
        )

        contatos = (
            self.contato_service
            .listar_contatos()
        )

        self.contatos_dict = {
            contato["nome"]: contato["id"]
            for contato in contatos
        }

        nomes = list(
            self.contatos_dict.keys()
        )

        ctk.CTkLabel(
            formulario,
            text="Contato"
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.contato_combo = (
            ctk.CTkComboBox(
                formulario,
                values=nomes,
                width=450
            )
        )

        self.contato_combo.pack(
            padx=20,
            pady=(0, 10),
            anchor="w"
        )

        ctk.CTkLabel(
            formulario,
            text="Mensagem"
        ).pack(
            anchor="w",
            padx=20
        )

        self.mensagem_entry = (
            ctk.CTkTextbox(
                formulario,
                width=600,
                height=120
            )
        )

        self.mensagem_entry.pack(
            padx=20,
            pady=(5, 10),
            anchor="w"
        )

        data_hora_frame = (
            ctk.CTkFrame(
                formulario,
                fg_color="transparent"
            )
        )

        data_hora_frame.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

        data_frame = (
            ctk.CTkFrame(
                data_hora_frame,
                fg_color="transparent"
            )
        )

        data_frame.pack(
            side="left",
            padx=(0, 20)
        )

        ctk.CTkLabel(
            data_frame,
            text="Data"
        ).pack(
            anchor="w"
        )

        self.data_entry = (
            ctk.CTkEntry(
                data_frame,
                width=150
            )
        )

        self.data_entry.pack()

        hora_frame = (
            ctk.CTkFrame(
                data_hora_frame,
                fg_color="transparent"
            )
        )

        hora_frame.pack(
            side="left"
        )

        ctk.CTkLabel(
            hora_frame,
            text="Hora"
        ).pack(
            anchor="w"
        )

        self.hora_entry = (
            ctk.CTkEntry(
                hora_frame,
                width=120
            )
        )

        self.hora_entry.pack()

        self.btn_agendar = (
            ctk.CTkButton(
            formulario,
            text="Agendar",
            command=self.agendar
        )
        )

        self.btn_agendar.pack(
            padx=20,
            pady=20,
            anchor="w"
        )
        
     
    def agendar(self):

        nome = (
            self.contato_combo.get()
        )

        contato_id = (
            self.contatos_dict[nome]
        )

        mensagem = (
            self.mensagem_entry.get(
                "1.0",
                "end"
            ).strip()
        )

        data_envio = (
            self.data_entry.get()
        )

        hora_envio = (
            self.hora_entry.get()
        )

        self.agendamento_service.criar_agendamento(
            contato_id,
            mensagem,
            data_envio,
            hora_envio
        )

        print(
            "Agendamento salvo!"
        )   