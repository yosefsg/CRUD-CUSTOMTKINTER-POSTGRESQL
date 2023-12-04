import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_creditos import TablaCredito  
from components.tabla_trabajos import TablaTrabajos

class OptionsFrame(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.configure(corner_radius=0, fg_color=colors.grey)
        
        ctk.CTkButton(self,
                      width=140,
                      height=32,
                      text="Nuevo Crédito",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      font=("Helvetica", 15),
                      command=lambda: change_page("NuevoCredito")
        ).pack(padx=20, pady=15, side="right", anchor='ne')
        
        self.pack(fill='x')
        

class Creditos(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.configure(corner_radius=0, fg_color=colors.grey)
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        # Cabecera con título
        Header(self, "Crédito")
        
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        OptionsFrame(self, change_page)
        
        TablaCredito(self, change_page)  
        
        self.pack(fill='both', expand=True)