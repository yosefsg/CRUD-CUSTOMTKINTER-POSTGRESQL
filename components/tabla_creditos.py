import customtkinter as ctk
import colors
from tkfontawesome import icon_to_image
import functools

class TablaCredito(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.parent = parent
        self.change_page = change_page
        self.configure(corner_radius=0, fg_color=colors.grey)
        _abonar_icon = icon_to_image('money-bill', fill=colors.grey, scale_to_width=16)
        
        # Encabezados de la tabla
        headers = ["ID Crédito", "ID Cliente", "Fecha", "Límite de Pago", "Total", "Restante"]
        
        # Crear etiquetas para los encabezados
        for col, header in enumerate(headers):
            etiqueta = ctk.CTkLabel(self, text=header, width=30, text_color=colors.darkbrown, font=("Helvetica", 18, "bold"))
            etiqueta.grid(row=0, column=col, sticky='wn')

            fetch_credito = parent.conn.getCredits()  # Reemplaza con la función adecuada de postgres.py

        # Organizar los datos
        data = [(
            credito['idcredito'],
            credito['idcliente'],
            credito['fecha'],
            credito['limitepago'],
            "$"+str(credito['totalapagar']),
            ("$"+(str(credito['restante']) if credito['restante'] != None else str(credito['totalapagar']))
            
            ))
            for credito in fetch_credito]

        # Mostrar datos en la tabla
        for i, fila in enumerate(data, start=1):
            for j, valor in enumerate(fila):
                etiqueta = ctk.CTkLabel(self, text=str(valor), font=("Helvetica", 16))
                etiqueta.grid(row=i, column=j, sticky='w')
                
            ctk.CTkButton(self,
                image=_abonar_icon,
                text="",
                fg_color=colors.darkbrown,
                hover_color=colors.brown,
                width=10,
                height=10,
                corner_radius=20,
                command=functools.partial(self.editAppointment, data[i-1][0])).grid(row=i, column=j, sticky='e')

        # Ajustar el tamaño de las columnas
        self.grid_columnconfigure(0, weight=1)  # ID Crédito
        self.grid_columnconfigure(1, weight=1)  # ID Cliente
        self.grid_columnconfigure(2, weight=1)  # Fecha
        self.grid_columnconfigure(3, weight=1)  # Límite de Pago
        self.grid_columnconfigure(4, weight=1)  # Límite de Pago
        self.grid_columnconfigure(5, weight=1)  # Límite de Pago

        self.pack(expand=True, fill='both', anchor='ne')
        
    def editAppointment(self, idcredito):
        credito = self.parent.conn.getCredit(idcredito)
        
        self.change_page("Abonos", credito)
