import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
from components.tabla_trabajos import TablaTrabajos

class LeftForm(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        info = dict(*args)
        
        ctk.CTkLabel(self, text="Nombre", font=("Helvetica", 25)).pack(anchor='w')
        self.nombre = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.nombre.pack(pady=15, anchor='w')
        
        try:
            self.nombre.insert(0, info['idcliente'])
        except Exception as e:
            print("No args: ", e)
            
        ctk.CTkLabel(self, text="Apellido Paterno", font=("Helvetica", 25)).pack(anchor='w')
        self.apellidop = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.apellidop.pack(pady=15, anchor='w')
        
        try:
            self.apellidop.insert(0, info['apellidop'])
        except:
            print("No args")
        
        ctk.CTkLabel(self, text="Apellido Materno", font=("Helvetica", 25)).pack(anchor='w')
        self.apellidom = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.apellidom.pack(pady=15, anchor='w')
        
        try:
            self.apellidom.insert(0, info['apellidom'])
        except:
            print("No args")
        
        self.pack(side='left', padx=20, pady=20, anchor='nw')
        
        ctk.CTkLabel(self, text="Teléfono", font=("Helvetica", 25)).pack(anchor='w')
        self.telefono = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.telefono.pack(pady=15, anchor='w')
        
        try:
            self.telefono.insert(0, info['telefono'])
        except:
            print("No args")
        
        self.pack(padx=10, pady=20, anchor='center')
        
        ctk.CTkLabel(self, text="Correo", font=("Helvetica", 25)).pack(anchor='w')
        self.correo = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.correo.pack(pady=15, anchor='w')
        
        try:
            self.correo.insert(1.0, info['correo'])
        except Exception as e:
            print("No args: ", e)
        
        self.pack(side='left', padx=20, pady=20, anchor='nw')
        
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "nombre": self.nombre,
            "apellidop": self.apellidop,
            "apellidom": self.apellidom,
            "telefono": self.telefono,
            "correo": self.correo
        }
        
class RightForm(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        info = dict(*args)
        
        ctk.CTkLabel(self, text="Calle", font=("Helvetica", 25)).pack(anchor='w')
        self.calle = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.calle.pack(pady=15, anchor='w')
        
        try:
            self.calle.insert(0, info['calle'])
        except:
            print("No args")
        
        
        ctk.CTkLabel(self, text="Número Exterior", font=("Helvetica", 25)).pack(anchor='w')
        self.numext = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.numext.pack(pady=15, anchor='w')
        
        try:
            self.numext.insert(0, info['numext'])
        except Exception as e:
            print("No args: ", e)
        
        ctk.CTkLabel(self, text="Número Interior", font=("Helvetica", 25)).pack(anchor='w')
        self.numint = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.numint.pack(pady=15, anchor='w')
        
        try:
            self.numint.insert(0, info['numint'])
        except Exception as e:
            print("No args: ", e)
        
        
        ctk.CTkLabel(self, text="Colonia", font=("Helvetica", 25)).pack(anchor='w')
        self.colonia = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.colonia.pack(pady=15, anchor='w')
        
        try:
            self.colonia.insert(0, info['colonia'])
        except:
            print("No args")
            
        ctk.CTkLabel(self, text="Código Postal", font=("Helvetica", 25)).pack(anchor='w')
        self.codigopostal = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.codigopostal.pack(pady=15, anchor='w')
        
        try:
            self.codigopostal.insert(1.0, info['codigopostal'])
        except:
            print("No args")
        
        self.pack(side='right', padx=20, pady=20, anchor='nw')
    
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "calle": self.calle,
            "numext": self.numext,
            "numint": self.numint,
            "colonia": self.colonia,
            "codigpostal": self.codigopostal,
        }

class NewClientFrame(ctk.CTkScrollableFrame):
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

class RegistroCliente(ctk.CTkFrame):
    def __init__(self, parent, change_page, *args):
        super().__init__(parent)
        
        # Recuperando el ID de la cita si es que se desea editar un registro
        try:
            self.idcliente = dict(*args)['idcliente']
        except:
            self.idcliente = None
        
        # Para cambiar de pantalla
        self.change_page = change_page

        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Registrar Cliente")
        
        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
        fields = NewClientFrame(self, args).getValues()
        
        # Boton para registrar cita
        ctk.CTkButton(self,
                      width=250,
                      height=45,
                      text="Registrar",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      text_color=colors.white,
                      font=("Helvetica", 25, 'bold'),
                      command=lambda: self.sendInfo(fields)
        ).pack(pady=15, padx=20, side="bottom", anchor='center')
        
        self.pack(fill='both', expand=True)

    def sendInfo(self, fields):
        
        # Si es el caso de editar una cita
        if self.idcliente != None:
            return self.editInfo(fields)
        
        self.conn.postAppointments((
            fields['idcliente'].get(),
            fields['fecha'].get(),
            fields['cotizacion'].get(),
            fields['descripcion'].get("1.0", "end-1c"),
            fields['lugar'].get("1.0", "end-1c")            
        ))
        
        # Cambia a la screen de trabajos
        
        self.change_page("Trabajos")
        
    def editInfo(self, fields):
        self.conn.putAppointment(
            self.idcliente,
            (
            fields['idcliente'].get(),
            fields['fecha'].get(),
            fields['cotizacion'].get(),
            fields['descripcion'].get("1.0", "end-1c"),
            fields['lugar'].get("1.0", "end-1c")            
        ))
        
        # Cambia a la screen de trabajos
        
        self.change_page("Trabajos")
