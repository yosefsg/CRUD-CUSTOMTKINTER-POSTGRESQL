import customtkinter as ctk
import colors

class Historial(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0)
        
        ctk.CTkLabel(self, text="HISTORIAL").pack()
        
        self.pack(fill='both', expand=True)