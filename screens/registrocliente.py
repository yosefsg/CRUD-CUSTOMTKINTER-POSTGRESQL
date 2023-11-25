import customtkinter as ctk
import colors
from components.header import Header

class Contenido(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # Crear dos columnas para los campos
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=1, column=0, padx=10)
        
        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=1, column=1, padx=10)
        
        # Campos de la izquierda
        ctk.CTkLabel(left_frame, text="ID:").pack()
        self.id_entry = ctk.CTkEntry(left_frame)
        self.id_entry.pack()
        
        ctk.CTkLabel(left_frame, text="Nombre:").pack()
        self.nombre_entry = ctk.CTkEntry(left_frame)
        self.nombre_entry.pack()
        
        ctk.CTkLabel(left_frame, text="Apellido Paterno:").pack()
        self.apellido_p_entry = ctk.CTkEntry(left_frame)
        self.apellido_p_entry.pack()
        
        ctk.CTkLabel(left_frame, text="Apellido Materno:").pack()
        self.apellido_m_entry = ctk.CTkEntry(left_frame)
        self.apellido_m_entry.pack()
        
        # Campos de la derecha
        ctk.CTkLabel(right_frame, text="Calle:").pack()
        self.calle_entry = ctk.CTkEntry(right_frame)
        self.calle_entry.pack()
        
        ctk.CTkLabel(right_frame, text="Colonia:").pack()
        self.colonia_entry = ctk.CTkEntry(right_frame)
        self.colonia_entry.pack()
        
        ctk.CTkLabel(right_frame, text="Código Postal:").pack()
        self.cp_entry = ctk.CTkEntry(right_frame)
        self.cp_entry.pack()
        
        ctk.CTkLabel(right_frame, text="Número Exterior:").pack()
        self.num_ext_entry = ctk.CTkEntry(right_frame)
        self.num_ext_entry.pack()
        
        # Campo común para ambas columnas
        ctk.CTkLabel(self, text="Teléfono:").grid(row=2, column=0)
        self.telefono_entry = ctk.CTkEntry(self)
        self.telefono_entry.grid(row=2, column=1)
        
        ctk.CTkLabel(self, text="Correo Electrónico:").grid(row=3, column=0)
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.grid(row=3, column=1)
        
        # Botón de envío
        submit_button = ctk.CTkButton(self, text="Enviar", command=self.enviar_registro)
        submit_button.grid(row=4, column=0, columnspan=2)
        
        self.pack(expand=True, fill='both')
        
    def enviar_registro(self):
        # Obtener los valores de todos los campos
        id_cliente = self.id_entry.get()
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_p_entry.get()
        apellido_materno = self.apellido_m_entry.get()
        calle = self.calle_entry.get()
        colonia = self.colonia_entry.get()
        cp = self.cp_entry.get()
        num_ext = self.num_ext_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()
        
        # Aquí podrías realizar las acciones para guardar estos datos en una base de datos u otro procesamiento necesario.
        print(f"Registrando cliente - ID: {id_cliente}, Nombre: {nombre}, Apellido Paterno: {apellido_paterno}, Apellido Materno: {apellido_materno}, Calle: {calle}, Colonia: {colonia}, CP: {cp}, Número Exterior: {num_ext}, Teléfono: {telefono}, Correo: {email}")
        

class RegistroCliente(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=0)
        
        # Cabecera con título
        Header(self, "Registro de clientes") 
          
        # Contenido para el registro de clientes
        Contenido(self)
        
        
        self.pack(fill='both', expand=True)
    
    

