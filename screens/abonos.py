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
        
        ctk.CTkLabel(self, text="ID Crédito", font=("Helvetica", 25)).pack(anchor='w')
        self.idcredito = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.idcredito.pack(pady=15, anchor='w')
        
        try:
            self.idcredito.insert(0, info['idcredito'])
        except Exception as e:
            print("No idcredito: ", e)
            
        ctk.CTkLabel(self, text="Monto a abonar", font=("Helvetica", 25)).pack(anchor='w')
        self.monto = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.monto.pack(pady=15, anchor='w')
        
        try:
            self.monto.insert(0, info['monto'])
        except:
            print("No monto")
    
    def getValues(self):
        # Devuelve los campos de texto
        return {
            "idcredito": self.idcredito,
            "monto": self.monto
        }
            
class RightForm(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        info = dict(*args)
        
        ctk.CTkLabel(self, text="Total a pagar", font=("Helvetica", 25)).pack(anchor='w')
        self.totalapagar = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.totalapagar.pack(pady=15, anchor='w')
        
        try:
            self.totalapagar.insert(0, info['totalapagar'])
        except:
            print("No totalapagar")
        
        
        ctk.CTkLabel(self, text="Restante", font=("Helvetica", 25)).pack(anchor='w')
        self.restante = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.restante.pack(pady=15, anchor='w')
        
        try:
            self.restante.insert(0, info['restante'])
        except Exception as e:
            print("No restante: ", e)
        

    def getValues(self):
        # Devuelve los campos de texto
        return {
            "restante": self.restante,
            "totalapagar": self.totalapagar
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

        # Recuperando el ID del crédito si es que se desea editar un registro
        try:
            self.idabonos = dict(*args)['idcredito']
        except:
            self.idabonos = None

        # Para cambiar de pantalla
        self.change_page = change_page

        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Abonos")

        # Para consumir las "apis" y armar la conexión
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor

        fields = AbonosFrame(self, args).getValues()

        # Boton para registrar abono
        ctk.CTkButton(self,
                      width=250,
                      height=45,
                      text="Registrar Abono",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      text_color=colors.white,
                      font=("Helvetica", 20, 'bold'),
                      command=lambda: self.sendInfo(fields)
        ).pack(pady=15, padx=20, side="bottom", anchor='center')

        self.pack(fill='both', expand=True)

    def sendInfo(self, fields):
        # Si es el caso de editar un abono
        if self.idabonos is not None:
            return self.editInfo(fields)

        self.conn.postAbonos((
            fields['idcredito'].get(),
            fields['monto'].get(),
            fields['restante'].get(),
            fields['totalapagar'].get()  
        ))

        # Cambia a la pantalla de trabajos
        self.change_page("Trabajos")

    def editInfo(self, fields):
        self.conn.putAbonos(
            self.idabonos,
            (
                fields['idcredito'].get(),
                fields['monto'].get(),
                fields['restante'].get(),
                fields['totalapagar'].get()  
            ))

        # Cambia a la pantalla de trabajos
        self.change_page("Trabajos")