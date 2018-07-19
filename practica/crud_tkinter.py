# -*- coding: utf-8 -*-
# Aplicación CRUD con Tkinter

from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

# -------------- Creación de la barra de menú ----------------------------------------------------------
barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

# tearoff quita las lineas del menú
bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar")
bbdd_menu.add_command(label="Salir")

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar")

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de...")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

# -------------- Creación de elementos del formulario --------------------------------------------------

frame_campos = Frame(root)
frame_campos.pack()

id_l = Label(frame_campos, text="Id:")
id_l.grid(row=0, column=0, sticky="e", padx=10, pady=10)
id = Entry(frame_campos)
id.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()

