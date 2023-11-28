import customtkinter as ctk
import colors

class TablaTrabajos(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0, fg_color=colors.grey)
        headers = ["ID", "Cliente", "Fecha", "Cotizacion", "Lugar", "Descripcion" ]
        
        for col, header in enumerate(headers):
            etiqueta = ctk.CTkLabel(self, text=header, width=30, text_color=colors.darkbrown, font=("Helvetica", 18, "bold"))
            etiqueta.grid(row=0, column=col, sticky='wn')
        
        fetch_citas = parent.conn.selectAllAppointments()
        
        data = [(
                cita['idcita'],
                cita['idcliente'],
                cita['fecha'],
                cita['cotizacion'],
                cita['lugar'],
                cita['descripcion']
                )
                for cita in fetch_citas]
        

        for i, fila in enumerate(data, start=1):
            for j, valor in enumerate(fila):
                etiqueta = ctk.CTkLabel(self, text=valor, font=("Helvetica", 16))
                etiqueta.grid(row=i, column=j, sticky='w')
                
        self.grid_columnconfigure(0, weight=1) # ID
        self.grid_columnconfigure(1, weight=1) # Cliente
        self.grid_columnconfigure(2, weight=1) # Fecha
        self.grid_columnconfigure(3, weight=1) # Cotizacion
        self.grid_columnconfigure(4, weight=2) # Lugar
        self.grid_columnconfigure(5, weight=3) # Descripcion
        
        self.pack(expand=True, fill='both')