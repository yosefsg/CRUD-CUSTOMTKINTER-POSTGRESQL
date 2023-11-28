import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_creditos import TablaCreditos


class Creditos(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.configure(corner_radius=0)
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        # Cabecera con título
        Header(self, "Credito")
        
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        TablaCreditos(self)
        
        # ctk.CTkLabel(self, text="HISTORIAL").pack()
        
        self.pack(fill='both', expand=True)