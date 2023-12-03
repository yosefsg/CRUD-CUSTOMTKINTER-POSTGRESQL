import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_trabajos import TablaTrabajos
from tkcalendar import DateEntry
from tkcalendar import Calendar
from datetime import datetime
      
class Form(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        info = dict(*args)
        
        ctk.CTkLabel(self, text="ID Cliente", font=("Helvetica", 32)).pack()
        self.idcliente = ctk.CTkTextbox(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=40
                                     )
        self.idcliente.pack(pady=15)
        
        try:
            self.idcliente.insert(1.0, info['idcliente'])
        except:
            print("No idcliente")
            
        ctk.CTkLabel(self, text="Límite de pago", font=("Helvetica", 32)).pack()
        self.limitepago = DateEntry(self, width=30, background=colors.darkbrown, date_pattern='yyyy/mm/dd', font=("Helvetica", 14))
        self.limitepago.pack(padx=10, pady=10)
        
        try:
            self.limitepago.set_date(info['limitepago'])
        except:
            print("No limitepago")
        
        self.pack(padx=20, pady=20, anchor='center')
        
        ctk.CTkLabel(self, text="Total a pagar", font=("Helvetica", 32)).pack()
        self.totalapagar = ctk.CTkTextbox(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=40
                                     )
        self.totalapagar.pack(pady=15)
        
        try:
            self.totalapagar.insert(1.0, info['totalapagar'])
        except:
            print("No totalapagar")
        
    
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "idcliente": self.idcliente,
            "limitepago": self.limitepago,
            "totalapagar": self.totalapagar
        }


class NuevoCreditoFrame(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(corner_radius=15, fg_color=colors.white)
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        # Frame para la parte de la izquierda XD
        self.form = Form(self, args).getValues()
        
        self.pack(fill='both', expand=True, padx=20, pady=20)
        
    def getValues(self):
        return {**self.form}

class NuevoCredito(ctk.CTkFrame):
    def __init__(self, parent, change_page, *args): 
        super().__init__(parent)
        
        # Recuperando el ID de la cita si es que se desea editar un registro
        try:
            self.idcredito = dict(*args)['idcredito']
        except:
            self.idcredito = None
        
        # Para cambiar de pantalla
        self.change_page = change_page

        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Nuevo Crédito")
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        fields = NuevoCreditoFrame(self, args).getValues()
        
        # Boton para registrar cita
        ctk.CTkButton(self,
                      width=250,
                      height=45,
                      text="Registrar",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      text_color=colors.white,
                      font=("Helvetica", 20, 'bold'),
                      command=lambda: self.sendInfo(fields)
        ).pack(pady=15, padx=20, side="bottom", anchor='center')
        
        self.pack(fill='both', expand=True)

    def sendInfo(self, fields):
        
        # Si es el caso de editar una cita
        if self.idcredito != None:
            return self.editInfo(fields)
        
        self.conn.postCredit((
            fields['idcliente'].get(),
            datetime.now().date(), # Fecha de hoy
            fields['limitepago'].get(),
            fields['totalapagar'].get()           
        ))
        
        # Cambia a la screen de trabajos
        
        self.change_page("Creditos")
        
    def editInfo(self, fields):
        self.conn.postCredit(
            self.idcredito,
            (
            fields['idcliente'].get(),
            datetime.now().date(), # Fecha de hoy
            fields['limitepago'].get(),
            fields['totalapagar'].get()           
        ))
        
        # Cambia a la screen de trabajos
        
        self.change_page("Trabajos")
