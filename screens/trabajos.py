import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_trabajos import TablaTrabajos


class Trabajos(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Citas Pendientes")
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        ctk.CTkButton(self,
                      width=140,
                      height=32,
                      text="Agregar Cita",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      font=("Helvetica", 15),
                      command=lambda: self.change_page("AgendarCita")
        ).pack(padx=20, pady=15, side="top", anchor='e')
        
        TablaTrabajos(self)
        
        self.pack(fill='both', expand=True)
