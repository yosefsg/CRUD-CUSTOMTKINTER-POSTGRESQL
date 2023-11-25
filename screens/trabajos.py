import customtkinter as ctk
import colors
from components.header import Header

class Tabla(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ctk.CTkLabel(self, text="Esto es una prueba", font=("Helvetica", 20)).pack(side='top', anchor='nw', pady=25, padx=25)
        
        self.pack(expand=True, fill='both')

class Trabajos(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0)
        Header(self, "Citas Pendientes")
        
        Tabla(self)
        
        self.pack(fill='both', expand=True)