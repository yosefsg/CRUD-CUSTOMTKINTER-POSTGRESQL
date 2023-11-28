import customtkinter as ctk
import colors
from components.sidebar import SideBar
from stack import PageStack

class App(ctk.CTk):
    def __init__(self, w, h):
        super().__init__()
        
        # Configurando la ventana
        _xWin = (self.winfo_screenwidth() // 2) - (w//2)
        _yWin = (self.winfo_screenheight() // 2) - (h//2)
        self.geometry(f'{w}x{h}+{_xWin}+{_yWin}')
        self.config(bg=colors.white)
        self.title("Proyecto SBD")
        
        # Instanciando el stack de las screens
        _stack = PageStack(self)    
        
        # Controlador de las pantallas
        SideBar(self, _stack)
        
        self.mainloop()


if __name__ == '__main__':
    
    App(1080, 580)