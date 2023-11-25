import customtkinter as ctk
import colors
from components.header import Header


class Inventario(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0)
        
        # Cabecera con título
        Header(self, "Inventario")
        
        ctk.CTkLabel(self, text="INVENTARIO").pack()
        
        self.pack(fill='both', expand=True)