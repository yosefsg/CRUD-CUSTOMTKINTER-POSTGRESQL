import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_inventario import TablaInventario


class Inventario(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.configure(corner_radius=0, fg_color=colors.grey)
        # Cabecera con título
        Header(self, "Inventario")
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        ctk.CTkButton(self,
                      width=140,
                      height=32,
                      text="Agregar al inventario",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      font=("Helvetica", 15), command=lambda: change_page ("NuevoInventarioFrame")
        ).pack(padx=20, pady=15, side="top", anchor='e')
        
        TablaInventario(self)
        
        # ctk.CTkLabel(self, text="INVENTARIO").pack()
        
        self.pack(fill='both', expand=True)