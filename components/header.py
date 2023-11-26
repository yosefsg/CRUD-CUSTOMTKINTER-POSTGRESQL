import customtkinter as ctk
import colors

class Header(ctk.CTkFrame):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.configure(fg_color=colors.brown, corner_radius=0)
        ctk.CTkLabel(self, text=title, font=("Helvetica", 40), text_color=colors.white).pack(side='top', anchor='nw', pady=20, padx=25)
        
        self.pack(fill='x', anchor='n', side='top')
