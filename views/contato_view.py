
import customtkinter as ctk

from services.contato_service import (
    ContatoService
)

class ContatoView(ctk.CTkFrame):

    def __init__(
        self,
        master
    ):
        super().__init__(master)

        self.service = ContatoService()

        self.pack(
            fill="both",
            expand=True            
        )

        self.criar_componentes()
        
        self.carregar_contatos()
        

    def criar_componentes(self):

        ctk.CTkLabel(
            self,
            text="Nome"
        ).pack()

        self.nome_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.nome_entry.pack(
            pady=5
        )

        ctk.CTkLabel(
            self,
            text="Telefone"
        ).pack()

        self.telefone_entry = ctk.CTkEntry(
            self,
            width=300
        )

        self.telefone_entry.pack(
            pady=5
        )
        
        
        ctk.CTkButton(
            self,
            text="Salvar",
            command=self.salvar
        ).pack(
            pady=20
        )
        
        
        ctk.CTkLabel(
            self,
            text="Contatos Cadastrados",
            font=("Arial", 16, "bold")
        ).pack(
            pady=(20,10)
        )
        
        
        self.lista_contatos = ctk.CTkTextbox(
            self,
            width=600,
            height=250
        )

        self.lista_contatos.pack(
            pady=10
        )
     
     
    def carregar_contatos(self):

        self.lista_contatos.delete(
            "1.0",
            "end"
        )

        contatos = (
            self.service.listar_contatos()
        )

        for contato in contatos:

            texto = (
                f"{contato['id']} - "
                f"{contato['nome']} - "
                f"{contato['telefone']}\n"
            )

            self.lista_contatos.insert(
                "end",
                texto
            )   


    def salvar(self):

        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()

        if not nome.strip():
            print("Telefone obrigatório")
            return
        
        if not telefone.strip():
            print("Telefone obrigatório")
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
        

        print("Contato salvo!")
        
        
        self.nome_entry.delete(0, "end")
        self.telefone_entry.delete(0, "end")
        
        
        
    