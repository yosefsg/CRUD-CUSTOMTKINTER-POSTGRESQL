import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from tkcalendar import DateEntry
from tkcalendar import Calendar

class LeftForm(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        ctk.CTkLabel(self, text="ID Cliente", font=("Helvetica", 32)).pack()
        self.id_cliente = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=200, height=40)
        self.id_cliente.pack(pady=15)
        
        info = dict(*args)
        
        try:
            self.id_cliente.insert(0, info['idcliente'])
        except Exception as e:
            print("No idcliente: ", e)
        
        ctk.CTkLabel(self, text="Fecha", font=("Helvetica", 32)).pack()
        self.fecha = DateEntry(self, width=16, background=colors.darkbrown, date_pattern='yyyy/mm/dd', font=("Helvetica", 14))
        self.fecha.pack(padx=10, pady=10)
        
        try:
            self.fecha.set_date(info['fecha'])
        except:
            print("No fecha")
        
        ctk.CTkLabel(self, text="Cotizacion", font=("Helvetica", 32)).pack()
        self.cotizacion = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=200, height=40)
        self.cotizacion.pack(pady=15)
        
        try:
            self.cotizacion.insert(0, info['cotizacion'])
        except:
            print("No cotizacion")
        
        self.pack(side='left', padx=20, pady=20, anchor='nw')
        
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "idcliente": self.id_cliente,
            "fecha": self.fecha,
            "cotizacion": self.cotizacion
        }
        
class RightForm(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        info = dict(*args)
        
        ctk.CTkLabel(self, text="Descripcion", font=("Helvetica", 32)).pack()
        self.descripcion = ctk.CTkTextbox(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=140
                                     )
        self.descripcion.pack(pady=15)
        
        try:
            self.descripcion.insert(1.0, info['descripcion'])
        except:
            print("No descripcion")
        
        
        ctk.CTkLabel(self, text="Lugar", font=("Helvetica", 32)).pack()
        self.lugar = ctk.CTkTextbox(self,
                                     fg_color=colors.grey,
                                     border_width=1,
                                     corner_radius=7,
                                     width=350,
                                     height=50
                                     )
        self.lugar.pack(pady=15)
        
        try:
            self.lugar.insert(1.0, info['lugar'])
        except Exception as e:
            print("No lugar: ", e)
        
        self.pack(side='right', padx=20, pady=20, anchor='nw')
        
    
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "descripcion": self.descripcion,
            "lugar": self.lugar
        }


class AbonosFrame(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(corner_radius=15, fg_color=colors.white)
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        # Frame para la parte de la izquierda XD
        self.left = LeftForm(self, args).getValues()
        
        # Frame para la parte de la derecha XD
        self.right = RightForm(self, args).getValues()
        
        self.pack(fill='both', expand=True, padx=20, pady=20)
        
    def getValues(self):
        return {**self.left, **self.right}

class Abonos(ctk.CTkFrame):
    def __init__(self, parent, change_page, *args): 
        super().__init__(parent)
        
        # Recuperando el ID de la cita si es que se desea editar un registro
        try:
            self.idcita = dict(*args)['idcita']
        except:
            self.idcita = None
        
        # Para cambiar de pantalla
        self.change_page = change_page

        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Agregar Cita")
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        fields = AbonosFrame(self, args).getValues()
        
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
        if self.idcita != None:
            return self.editInfo(fields)
        
        self.conn.postAppointments((
            fields['idcliente'].get(),
            fields['fecha'].get_date(),
            fields['cotizacion'].get(),
            fields['descripcion'].get("1.0", "end-1c"),
            fields['lugar'].get("1.0", "end-1c")            
        ))
        
        # Cambia a la screen de trabajos
        
        self.change_page("Creditos")
        
    def editInfo(self, fields):
        self.conn.putAppointment(
            self.idcita,
            (
            fields['idcliente'].get(),
            fields['fecha'].get(),
            fields['cotizacion'].get(),
            fields['descripcion'].get("1.0", "end-1c"),
            fields['lugar'].get("1.0", "end-1c")            
        ))
        
        # Cambia a la screen de trabajos
        
        self.change_page("Creditos")