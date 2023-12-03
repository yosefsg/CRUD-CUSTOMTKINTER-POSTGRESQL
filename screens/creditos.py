import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_creditos import TablaCredito  
from components.tabla_trabajos import TablaTrabajos

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
        
        ctk.CTkButton(self,
                      width=140,
                      height=32,
                      text="Abonar",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      font=("Helvetica", 15),
                      command=lambda: self.change_page("AgendarCita")
        ).pack(padx=20, pady=15, side="top", anchor='e')
        
         ctk.CTkButton(self,
                      width=140,
                      height=32,
                      text="Añadir Crédito",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      font=("Helvetica", 15),
                      command=lambda: self.change_page("Abonos")
        ).pack(padx=5, pady=1, side="top", anchor='e')
        
        TablaCredito(self)  
        
        # ctk.CTkLabel(self, text="CRÉDITO").pack()
        
        self.pack(fill='both', expand=True)