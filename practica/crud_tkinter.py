# -*- coding: utf-8 -*-
# Aplicación CRUD con Tkinter

from tkinter import *
from tkinter import messagebox
import sqlite3


def conexionBBDD():
    conexion = sqlite3.connect("ventas.bd")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
           CREATE TABLE  usuarios (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              nombre VARCHAR(50),
              apellido VARCHAR(100),
              domicilio VARCHAR(100),
              password VARCHAR(50),
              comentario VARCHAR(100)
              )
          ''')
        messagebox.showinfo("BBDD", "Base de datos creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La base de datos ya existe")


def cerrar_app():
    salir = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if salir == "yes":
        root.destroy()


def limpiar_form():
    id.set("")
    nombre.set("")
    apellido.set("")
    domicilio.set("")
    clave.set("")
    # Como borrar un cuadro de texto, desde el 1.0
    comentario_f.delete(1.0, END)


def crear():
    conexion = sqlite3.connect("ventas.bd")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios VALUES (NULL, "
                   "'" + nombre.get() +
                   "', '" + apellido.get() +
                   "', '" + domicilio.get() +
                   "', '" + clave.get() +
                   "', '" + comentario_f.get(1.0, END) + "')"
                   )
    conexion.commit()
    messagebox.showinfo("BBDD", "¡Registro insertado con éxito!")


root = Tk()

# -------------- Creación de la barra de menú ----------------------------------------------------------
barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

# tearoff quita las lineas del menú
bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexionBBDD)
bbdd_menu.add_command(label="Salir", command=cerrar_app)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Limpiar", command=limpiar_form)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_command(label="Acerca de...")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Formulario", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

# -------------- Creación de elementos del formulario --------------------------------------------------

frame_campos = Frame(root)
frame_campos.pack()

# ------------ Definimos las variables para cada campo -----------------------------------

id = StringVar()
nombre = StringVar()
apellido = StringVar()
domicilio = StringVar()
clave = StringVar()
# comentario = StringVar() - No es necesario ya que es del tipo text

id_l = Label(frame_campos, text="Id:")
id_l.grid(row=0, column=0, sticky="e", padx=10, pady=10)
id_f = Entry(frame_campos, textvariable=id)
id_f.grid(row=0, column=1, padx=10, pady=10)

nombre_l = Label(frame_campos, text="Nombre:")
nombre_l.grid(row=1, column=0, sticky="e", padx=10, pady=10)
nombre_f = Entry(frame_campos, textvariable=nombre)
nombre_f.grid(row=1, column=1, padx=10, pady=10)
nombre_f.config(fg="red", justify="right")

apellido_l = Label(frame_campos, text="Apellido:")
apellido_l.grid(row=2, column=0, sticky="e", padx=10, pady=10)
apellido_f = Entry(frame_campos, textvariable=apellido)
apellido_f.grid(row=2, column=1, padx=10, pady=10)

domicilio_l = Label(frame_campos, text="Domicilio:")
domicilio_l.grid(row=3, column=0, sticky="e", padx=10, pady=10)
domicilio_f = Entry(frame_campos, textvariable=domicilio)
domicilio_f.grid(row=3, column=1, padx=10, pady=10)

clave_l = Label(frame_campos, text="Contraseña:")
clave_l.grid(row=4, column=0, sticky="e", padx=10, pady=10)
clave_f = Entry(frame_campos, textvariable=clave)
clave_f.grid(row=4, column=1, padx=10, pady=10)
clave_f.config(show="*")

comentarios_l = Label(frame_campos, text="Comentario:")
comentarios_l.grid(row=5, column=0, sticky="e", padx=10, pady=10)
comentario_f = Text(frame_campos, width=20, height=5)
comentario_f.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(frame_campos, command=comentario_f.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

comentario_f.config(yscrollcommand=scrollVert.set)

# -------------- Creación de botones de acciòn --------------------------------------------------
frame_btn = Frame(root)
frame_btn.pack()

create_btn = Button(frame_btn, text="Create", command=crear)
create_btn.grid(row=0, column=0, sticky="e", padx=10, pady=10)

read_btn = Button(frame_btn, text="Read")
read_btn.grid(row=0, column=1, sticky="e", padx=10, pady=10)

update_btn = Button(frame_btn, text="Update")
update_btn.grid(row=0, column=2, sticky="e", padx=10, pady=10)

delete_btn = Button(frame_btn, text="Delete")
delete_btn.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()

