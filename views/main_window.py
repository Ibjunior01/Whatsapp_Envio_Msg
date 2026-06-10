# Janela principal

import customtkinter as ctk

from views.contato_view import (
    ContatoView
)

class MainWindow(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(
            "WhatsApp Scheduler Pro"
        )
        
        self.geometry(
            "1000x600"
        )
        
        ContatoView(self)