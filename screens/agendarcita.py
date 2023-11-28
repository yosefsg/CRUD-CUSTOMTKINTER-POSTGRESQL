import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_trabajos import TablaTrabajos

class LeftForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        ctk.CTkLabel(self, text="ID Cliente", font=("Helvetica", 32)).pack()
        id_cliente = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=200, height=40)
        id_cliente.pack(pady=15)
        
        ctk.CTkLabel(self, text="Fecha", font=("Helvetica", 32)).pack()
        fecha = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=200, height=40)
        fecha.pack(pady=15)
        
        ctk.CTkLabel(self, text="Cotizacion", font=("Helvetica", 32)).pack()
        cotizacion = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=200, height=40)
        cotizacion.pack(pady=15)
        
        self.pack(side='left', padx=20, pady=20, anchor='nw')
        
class RightForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        ctk.CTkLabel(self, text="Descripcion", font=("Helvetica", 32)).pack()
        descripcion = ctk.CTkTextbox(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=140
                                     )
        descripcion.pack(pady=15)
        
        ctk.CTkLabel(self, text="Lugar", font=("Helvetica", 32)).pack()
        lugar = ctk.CTkTextbox(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=50
                                     )
        lugar.pack(pady=15)
        
        self.pack(side='right', padx=20, pady=20, anchor='nw')

class AppointmentFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=15, fg_color=colors.white)
        
        # Frame para la parte de la izquierda XD
        LeftForm(self)
        
        # Frame para la parte de la derecha XD
        RightForm(self)
        
        self.pack(fill='both', expand=True, padx=20, pady=20)

class AgendarCita(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        
        # Para cambiar de pantalla
        self.change_page = change_page
        
        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Agregar Cita")
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        AppointmentFrame(self)
        
        # Boton para registrar cita
        ctk.CTkButton(self,
                      width=250,
                      height=45,
                      text="Registrar",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      text_color=colors.white,
                      font=("Helvetica", 20, 'bold')
        ).pack(pady=15, padx=20, side="bottom", anchor='center')
        
        self.pack(fill='both', expand=True)
