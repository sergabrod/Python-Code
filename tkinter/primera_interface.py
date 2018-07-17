# -*- coding: utf-8 -*-
# Trabajando con interfaces gráficas con Tkinter

from tkinter import *


raiz = Tk()
raiz.title("Tkinter con Python3")
# Restringir para no sea modificable el alto y el ancho
raiz.resizable(True, False)
# No funciona
raiz.iconbitmap('@postgresql.xbm')
# Ancho y alto de ventana
raiz.geometry("650x350")
# Bucle que mantiene la ventana en ejecución, debe estar siempre al final
raiz.mainloop()
