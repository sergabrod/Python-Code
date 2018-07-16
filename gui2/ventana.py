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
root.iconbitmap("@python3.xbm")
# Creo un frame y lo agrego a la raiz (root), antes debemos empaquetarlo
miFrame = Frame()
# anchor posiciona segùn los puntos cardinales, complento de side
miFrame.pack(side="bottom", anchor="w")
miFrame.config(bg="white")
miFrame.config(width="650", height="300")
miFrame.config(bd=5) # Borde
miFrame.config(cursor="hand2")
miFrame.config(relief="groove")
# Bucle infinito para permanecer a la escucha de eventos
root.mainloop()

