# -*- coding: utf-8 -*-
# utilizando widget menú

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Uso de Menúes")


def acerca_de():
    messagebox.showinfo("Sistema de Ventas", "SV - Python 2018")


def documentacion():
    messagebox.showwarning("Aviso!", "Documentación aún no disponible")


def salir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor == "yes":
        root.destroy()


def analizar_codigo():
    valor = messagebox.askokcancel("Analize", "Esto puede tardar mucho ¿Desea realizarlo de todos modos?")
    if valor:
        print("Analizando codigo....")
    else:
        print("Analisis cancelado.")


def ssh_session():
    valor = messagebox.askretrycancel("SSH", "No se puede establecer la conexión con el servidor")
    if valor:
        print("Intentando conectar son SSH....")
    else:
        print("Conexión SSH cancelada.")

barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

# ---- Creamos el menú ---------------------------------
archivo_menu = Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar como...")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar")
archivo_menu.add_command(label="Salir", command=salir)

edicion_menu = Menu(barra_menu, tearoff=0)
edicion_menu.add_command(label="Deshacer")
edicion_menu.add_command(label="Rehacer")
edicion_menu.add_separator()
edicion_menu.add_command(label="Cortar")
edicion_menu.add_command(label="Copiar")
edicion_menu.add_command(label="Pegar")
edicion_menu.add_separator()
edicion_menu.add_command(label="Buscar")
edicion_menu.add_command(label="Macros")

herramientas_menu = Menu(barra_menu, tearoff=0)
herramientas_menu.add_command(label="Consola")
herramientas_menu.add_command(label="Git")
herramientas_menu.add_separator()
herramientas_menu.add_command(label="SSH Session", command=ssh_session)
herramientas_menu.add_command(label="Deploy")
herramientas_menu.add_command(label="Analizar Código", command=analizar_codigo)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Documentación", command=documentacion)
ayuda_menu.add_command(label="Acerca de...", command=acerca_de)

# ------------------Agregamos a la barra--------------------
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edición", menu=edicion_menu)
barra_menu.add_cascade(label="Herramientas", menu=herramientas_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

root.mainloop()
