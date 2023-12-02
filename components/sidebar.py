# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:07:27 2023

@author: Avelar
"""

import customtkinter as ctk
import colors
from tkfontawesome import icon_to_image
from stack import PageStack

class SideBar(ctk.CTkFrame):
    def __init__(self, parent, stack):
        super().__init__(parent)
        
        # Recuperando el stack
        self.stack = stack
        
        # Haciendolo atributo de instancia
        self.parent = parent
        
        # Creando el sidebar
        self.create_sidebar()
        
        # Mostrando la pantalla de Trabajos por defecto
        self.stack.switch_page("Trabajos")
        
    def create_sidebar(self):
        # Iconos que se van a usar
        _userIcon = icon_to_image('user-circle', fill=colors.grey, scale_to_width=130)
        _toolsIcon = icon_to_image('tools', fill=colors.grey, scale_to_width=16)
        _clientIcon = icon_to_image('address-card', fill=colors.grey, scale_to_width=16)
        _historyIcon = icon_to_image('history', fill=colors.grey, scale_to_width=16)
        _toolboxIcon = icon_to_image('toolbox', fill=colors.grey, scale_to_width=16)        
        _creditsIcon = icon_to_image('credit-card', fill=colors.grey, scale_to_width=16)        
        
        self.configure(
            fg_color=colors.brown,
            corner_radius=0
            )
        
        # Lo que va arriba con el icono de admin        
        ctk.CTkLabel(self, image=_userIcon, text='').pack(padx=40, pady=(30, 10))
        ctk.CTkLabel(self, text="Administrador", text_color=colors.grey, font=('Helvetica', 20)).pack(pady=(0, 50))
                
        # Menú de navegación
        trabajos = ctk.CTkButton(
            self,
            text="Trabajos",
            text_color=colors.grey,
            font=('Helvetica', 19),
            image=_toolsIcon,
            compound="left",
            corner_radius=0,
            fg_color=colors.brown,
            hover_color=colors.darkbrown,
            height=57,
            anchor='w',
            command=lambda: self.stack.switch_page('Trabajos')
        ).pack(fill='x')
        
        registrarCliente = ctk.CTkButton(
            self,
            text="Clientes",
            text_color=colors.grey,
            font=('Helvetica', 19),
            image=_clientIcon,
            compound="left",
            corner_radius=0,
            fg_color=colors.brown,
            hover_color=colors.darkbrown,
            height=57,
            anchor='w',
            command=lambda: self.stack.switch_page('Clientes')
        ).pack(fill='x')
        
        historial = ctk.CTkButton(
            self,
            text="Historial",
            text_color=colors.grey,
            font=('Helvetica', 19),
            image=_historyIcon,
            compound="left",
            corner_radius=0,
            fg_color=colors.brown,
            hover_color=colors.darkbrown,
            height=57,
            anchor='w',
            command=lambda: self.stack.switch_page('Historial')
        ).pack(fill='x')
        
        inventario = ctk.CTkButton(
            self,
            text="Inventario",
            text_color=colors.grey,
            font=('Helvetica', 19),
            image=_toolboxIcon,
            compound="left",
            corner_radius=0,
            fg_color=colors.brown,
            hover_color=colors.darkbrown,
            height=57,
            anchor='w',
            command=lambda: self.stack.switch_page('Inventario')
        ).pack(fill='x')
        
        creditos = ctk.CTkButton(
            self,
            text="Créditos",
            text_color=colors.grey,
            font=('Helvetica', 19),
            image=_creditsIcon,
            compound="left",
            corner_radius=0,
            fg_color=colors.brown,
            hover_color=colors.darkbrown,
            height=57,
            anchor='w',
            command=lambda: self.stack.switch_page('Creditos')
        ).pack(fill='x', )
                
        self.pack(side='left', fill='y')
        
    