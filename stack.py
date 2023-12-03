from screens.trabajos import Trabajos
from screens.clientes import Clientes
from screens.registrocliente import RegistroCliente
from screens.historial import Historial
from screens.inventario import Inventario
from screens.creditos import Creditos
from screens.abonos import Abonos
from screens.agendarcita import AgendarCita
import customtkinter as ctk

class PageStack(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.pack(side='right', fill='both', expand=True)

    @property  
    def stack(self) -> dict:
        """
        Aquí se tienen que agregar las pantallas que vayamos a crear

        Args:
            screen (string): El nombre de la clase de la pantalla
        """
                
        return {
                "Trabajos": Trabajos,
                "Clientes": Clientes,
                "Historial": Historial,
                "Inventario": Inventario,
                "Creditos": Creditos,
                "AgendarCita": AgendarCita,
                "RegistroCliente": RegistroCliente,
                "Abonos": Abonos
                }
        
        
        
    def hide_pages(self):
        try:
            for frame in self.winfo_children():
                frame.destroy()
        except Exception as e:
            print("Error destroying screen from stack: ", e)
            
    def switch_page(self, screen, *args):
        # Limpiando la pantalla para hacer el cambio
        self.hide_pages()
        
        # print(self.stack[screen])
        # Cambiando de pantalla
        Current_screen = self.stack[screen]
        Current_screen(self, self.switch_page, *args)