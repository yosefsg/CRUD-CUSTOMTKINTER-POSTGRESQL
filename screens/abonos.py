import customtkinter as ctk
import colors
from components.header import Header
import controllers.postgres as pg
<<<<<<< HEAD
from components.tabla_trabajos import TablaTrabajos
=======
>>>>>>> b434637119dd49fe9b9ba8bae3634713888c1580

class Abonar(ctk.CTkFrame):
    def __init__(self, parent, args):
        super().__init__(parent)
        self.configure(fg_color=colors.white)
        
        info = dict(*args)
        
        ctk.CTkLabel(self, text="ID Crédito", font=("Helvetica", 25)).pack(anchor='w')
        self.id_credito = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.id_credito.pack(pady=15, anchor='w')
        
        try:
            self.id_credito.insert(0, info['id_credito'])
        except:
            print("No args")
            
        ctk.CTkLabel(self, text="Monto a Abonar", font=("Helvetica", 25)).pack(anchor='w')
        self.monto_abono = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.monto_abono.pack(pady=15, anchor='w')
        
        try:
            self.monto_abono.insert(0, info['monto_abono'])
        except:
            print("No args")
        
        
        
        ctk.CTkLabel(self, text="Total a Pagar", font=("Helvetica", 25)).pack(anchor='w')
        self.total_a_pagar = ctk.CTkEntry(self, fg_color=colors.grey, border_width=1, corner_radius=7, width=250, height=40)
        self.total_a_pagar.pack(pady=15, anchor='w')
        
        try:
            self.total_a_pagar.insert(0, info['total_a_pagar'])
        except:
            print("No args")
        
        self.pack(side='left', padx=20, pady=20, anchor='nw')
    
    def getValues(self):
        return {
            "id_credito": self.id_credito,
            "monto_abono": self.monto_abono,
            "total_a_pagar": self.total_a_pagar,
        }

<<<<<<< HEAD
class AbonoFrame(ctk.CTkFrame):
    def __init__(self, parent, change_page, args):
=======

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
>>>>>>> b434637119dd49fe9b9ba8bae3634713888c1580
        super().__init__(parent)
        
        try:
            self.id_abono = dict(args)['id_abono']
        except:
            self.id_abono = None
        
        # Para cambiar de pantalla
        self.change_page = change_page

        self.configure(corner_radius=0, fg_color=colors.grey)
        Header(self, "Realizar Abono")
        
        self.conn = pg.Connection()
        self.cursor = self.conn.cursor
        
<<<<<<< HEAD
        fields = AbonoForm(self, args).getValues()
=======
        fields = AbonosFrame(self, args).getValues()
>>>>>>> b434637119dd49fe9b9ba8bae3634713888c1580
        
        # Boton para realizar el abono
        ctk.CTkButton(self,
                      width=250,
                      height=45,
                      text="Realizar Abono",
                      fg_color=colors.darkbrown,
                      hover_color=colors.brown,
                      text_color=colors.white,
                      font=("Helvetica", 25, 'bold'),
                      command=lambda: self.sendInfo(fields)
        ).pack(pady=15, padx=20, side="bottom", anchor='center')
        
        self.pack(fill='both', expand=True)

    def sendInfo(self, fields):
        
        if self.id_abono is not None:
            return self.editInfo(fields)
        
        self.conn.postAbono((
            fields['id_credito'].get(),
            fields['monto_abono'].get(),
            fields['total_a_pagar'].get(),
            
        ))
        
<<<<<<< HEAD

=======
        # Cambia a la screen de trabajos
        
        self.change_page("Creditos")
        
>>>>>>> b434637119dd49fe9b9ba8bae3634713888c1580
    def editInfo(self, fields):
        # Lógica para editar un abono existente en la base de datos
        self.conn.putAbono(
            self.id_abono,
            (
                fields['id_credito'].get(),
                fields['monto_abono'].get(),
                fields['total_a_pagar'].get(),
            )
        )
        
<<<<<<< HEAD
        self.change_page("Creditos") 
=======
        # Cambia a la screen de trabajos
        
        self.change_page("Creditos")
>>>>>>> b434637119dd49fe9b9ba8bae3634713888c1580
