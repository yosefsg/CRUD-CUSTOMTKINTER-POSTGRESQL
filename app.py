import customtkinter as ctk
from dotenv import load_dotenv
import os
import colors
from components.sidebar import SideBar

# print(os.getenv("DB_NAME"))
class App(ctk.CTk):
    def __init__(self, w, h):
        super().__init__()
        
        # Configurando la ventana
        _xWin = (self.winfo_screenwidth() // 2) - (w//2)
        _yWin = (self.winfo_screenheight() // 2) - (h//2)
        self.geometry(f'{w}x{h}+{_xWin}+{_yWin}')
        self.config(bg=colors.white)
        self.resizable(False, False)
        # Mostrando el sidebar
        SideBar(self)
        
        self.mainloop()


if __name__ == '__main__':
    load_dotenv()
    App(1080, 580)