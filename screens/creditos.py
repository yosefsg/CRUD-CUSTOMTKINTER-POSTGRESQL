import customtkinter as ctk
import colors
from components.header import Header


class Creditos(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.configure(corner_radius=0)
        # Cabecera con título
        Header(self, "Créditos")
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        ctk.CTkLabel(self, text="CREDITOS").pack()
        
        self.pack(fill='both', expand=True)
        