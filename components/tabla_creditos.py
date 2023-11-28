import customtkinter as ctk
import colors

class TablaCreditos(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0, fg_color=colors.grey)
        
        # Estas son las cabeceras que indican qué va en cada columna
        headers = ["ID", "IDCliente", "Fecha", "Límite de pago" ]
        
        # Esta cosa hace que se muestren los headers en la app, creando objetos de Etiqueta por cada header 
        for col, header in enumerate(headers):
            etiqueta = ctk.CTkLabel(self, text=header, width=30, text_color=colors.darkbrown, font=("Helvetica", 18, "bold"))
            etiqueta.grid(row=0, column=col, sticky='wn')
        
        # Esto es importante, si van a hacer alguna tabla, usen el "get" correspondiente
        # En este caso, estoy trayendo todas las citas. Pueden ver cómo funciona en ./controllers/postgres.py
        fetch_creditos = parent.conn.getHistory() # Esto lo van a cambiar por el que corresponde a la pantalla
        
        # Este es el dataset que deberán organizar. Será usado para mostrarlo en la app
        # Con objetos de Etiqueta (ctk.CTkLabel)
        # Cambien la variable "cita" por cualquier otra cosa para que se entienda bien
        # Lo que está entre comillas simples es EL NOMBRE DE LA COLUMNA QUE VIENE EN NUESTRA BASE DE DATOS
        data = [(
                creditos['idcredito'],
                creditos['idcliente'],
                creditos['fecha'],
                creditos['limitedepago'],
                )
                for creditos in fetch_creditos]
        

        # Esto muestra en la app cada registro del dataset que armaron anteriormente.
        for i, fila in enumerate(data, start=1):
            for j, valor in enumerate(fila):
                etiqueta = ctk.CTkLabel(self, text=valor, font=("Helvetica", 16))
                etiqueta.grid(row=i, column=j, sticky='w')
                
        # Esto, también importante, es para modificar el tamaño horizontal de cada columna
        # De la siguiente función:
        #   self.grid_columnconfigure(0, weight=1)
        # - el primer parámetro (0) es el índice de la columna
        # - el segundo parámetro (weight=1) indica el tamaño horizontal que le toca A ESA COLUMNA EN ESPECIFICO
        
        self.grid_columnconfigure(0, weight=1) # ID
        self.grid_columnconfigure(1, weight=1) # Cliente
        self.grid_columnconfigure(2, weight=1) # Fecha
        self.grid_columnconfigure(3, weight=1) # Cotizacion
        self.grid_columnconfigure(5, weight=3) # Descripcion
        
        self.pack(expand=True, fill='both')