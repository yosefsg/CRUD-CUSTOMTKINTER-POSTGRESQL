import customtkinter as ctk
import colors

class Trabajos(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0)
        
        ctk.CTkLabel(self, text="TRABAJOS").pack()
        
        self.pack(fill='both', expand=True)