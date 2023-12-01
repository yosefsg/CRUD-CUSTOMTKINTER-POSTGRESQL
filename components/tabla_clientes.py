import customtkinter as ctk
import colors
import controllers.postgres as pg
from tkfontawesome import icon_to_image
import functools

class TablaClientes(ctk.CTkFrame):
    def __init__(self, parent, change_page):
        super().__init__(parent)
        self.parent = parent
        self.change_page = change_page
        self.configure(corner_radius=0, fg_color=colors.grey)
        
         # Iconos que se van a usar
        _edit_icon = icon_to_image('edit', fill=colors.grey, scale_to_width=16)
        _trash_icon = icon_to_image('trash-alt', fill=colors.grey, scale_to_width=16)
        
        # Estas son las cabeceras que indican qué va en cada columna
        headers = ["ID", "Nombre", "Telefono", "Dirección", "Correo"]
        
        # Esta cosa hace que se muestren los headers en la app, creando objetos de Etiqueta por cada header 
        for col, header in enumerate(headers):
            etiqueta = ctk.CTkLabel(self, text=header, width=30, text_color=colors.darkbrown, font=("Helvetica", 18, "bold"))
            etiqueta.grid(row=0, column=col, sticky='wn')
        
        # Esto es importante, si van a hacer alguna tabla, usen el "get" correspondiente
        # En este caso, estoy trayendo todas las citas. Pueden ver cómo funciona en ./controllers/postgres.py
        fetch_clientes = parent.conn.getClients() # Esto lo van a cambiar por el que corresponde a la pantalla
        
        # Este es el dataset que deberán organizar. Será usado para mostrarlo en la app
        # Con objetos de Etiqueta (ctk.CTkLabel)
        # Cambien la variable "cita" por cualquier otra cosa para que se entienda bien
        # Lo que está entre comillas simples es EL NOMBRE DE LA COLUMNA QUE VIENE EN NUESTRA BASE DE DATOS
        data = [(
                cliente['idcliente'],
                cliente['nombre']+' '+cliente['apellidop']+' '+cliente['apellidom'], # Nombre completo
                cliente['telefono'], # Telefono
                cliente['calle']+' '+cliente['numext']+ '. ' + cliente['colonia']+'. '+cliente['codigopostal'], # Dirección completa
                cliente['correo'] # Correo
                )
                for cliente in fetch_clientes]
        

        # Esto muestra en la app cada registro del dataset que armaron anteriormente.
        for i, fila in enumerate(data, start=1):
            for j, valor in enumerate(fila):
                etiqueta = ctk.CTkLabel(self, text=valor, font=("Helvetica", 16))
                etiqueta.grid(row=i, column=j, sticky='w')
                
            # Botón de editar
            ctk.CTkButton(self,
                        image=_edit_icon,
                        text="",
                        fg_color=colors.darkbrown,
                        width=10,
                        height=10,
                        corner_radius=20,
                        command=functools.partial(self.editClient, data[i-1][0])).grid(row=i, column=j, sticky='e')
            
            # Botón de eliminar
            ctk.CTkButton(self,
                        image=_trash_icon,
                        text="",
                        fg_color=colors.darkbrown,
                        width=10,
                        height=10,
                        corner_radius=20,
                        command=functools.partial(self.deleteClient, data[i-1][0])).grid(row=i, column=j+1, sticky='e')
                
        # Esto, también importante, es para modificar el tamaño horizontal de cada columna
        # De la siguiente función:
        #   self.grid_columnconfigure(0, weight=1)
        # - el primer parámetro (0) es el índice de la columna
        # - el segundo parámetro (weight=1) indica el tamaño horizontal que le toca A ESA COLUMNA EN ESPECIFICO
        
        self.grid_columnconfigure(0, weight=1) # ID
        self.grid_columnconfigure(1, weight=2) # Nombre
        self.grid_columnconfigure(2, weight=1) # Telefono
        self.grid_columnconfigure(3, weight=2) # Dirección
        self.grid_columnconfigure(4, weight=2) # Correo
        self.grid_columnconfigure(5, weight=1) # Boton edit
        self.grid_columnconfigure(6, weight=1) # Boton edit
        
        self.pack(expand=True, fill='both')
        
    def deleteClient(self, idcliente):
        self.parent.conn.deleteClient(str(idcliente))
        
        # Recarga la pantalla
        self.change_page("Clientes")
        
    def editClient(self, idcliente):
        client = self.parent.conn.getClient(idcliente)
        
        self.change_page("RegistroCliente", client)