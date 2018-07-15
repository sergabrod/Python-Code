# -*- coding: utf-8 -*-
# Trabajando con Tkinter

from tkinter import *

# Creamos la raiz del contenedor TK
root = Tk()
root.title("Tkinter con  Python")
root.geometry("650x500")
root.resizable(True, True)
# Cambia el color de fondo
root.config(bg="blue")
# root.iconbitmap("python.png")
# Bucle infinito para permanecer a la escucha de eventos
root.mainloop()

