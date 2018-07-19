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

nombre_l = Label(frame_campos, text="Nombre:")
nombre_l.grid(row=1, column=0, sticky="e", padx=10, pady=10)
nombre = Entry(frame_campos)
nombre.grid(row=1, column=1, padx=10, pady=10)
nombre.config(fg="red", justify="right")

apellido_l = Label(frame_campos, text="Apellido:")
apellido_l.grid(row=2, column=0, sticky="e", padx=10, pady=10)
apellido = Entry(frame_campos)
apellido.grid(row=2, column=1, padx=10, pady=10)

domicilio_l = Label(frame_campos, text="Domicilio:")
domicilio_l.grid(row=3, column=0, sticky="e", padx=10, pady=10)
domicilio = Entry(frame_campos)
domicilio.grid(row=3, column=1, padx=10, pady=10)

clave_l = Label(frame_campos, text="Contraseña:")
clave_l.grid(row=4, column=0, sticky="e", padx=10, pady=10)
clave = Entry(frame_campos)
clave.grid(row=4, column=1, padx=10, pady=10)
clave.config(show="*")

comentarios_l = Label(frame_campos, text="Comentario:")
comentarios_l.grid(row=5, column=0, sticky="e", padx=10, pady=10)
comentario = Text(frame_campos, width=20, height=5)
comentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(frame_campos, command=comentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

comentario.config(yscrollcommand=scrollVert.set)

# -------------- Creación de botones de acciòn --------------------------------------------------
frame_btn = Frame(root)
frame_btn.pack()

create_btn = Button(frame_btn, text="Create")
create_btn.grid(row=0, column=0, sticky="e", padx=10, pady=10)

read_btn = Button(frame_btn, text="Read")
read_btn.grid(row=0, column=1, sticky="e", padx=10, pady=10)

update_btn = Button(frame_btn, text="Update")
update_btn.grid(row=0, column=2, sticky="e", padx=10, pady=10)

delete_btn = Button(frame_btn, text="Delete")
delete_btn.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()

