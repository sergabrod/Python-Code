# -*- coding: utf-8 -*-
# Trabajando con Tkinter

from tkinter import *

# Creamos la raiz del contenedor TK
root = Tk()
root.title("Labels con Tkinter")
root.geometry("650x500")
root.resizable(True, True)

# Creo un frame y lo agrego a la raiz (root), antes debemos empaquetarlo
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

# Creamos el label
mi_label = Label(miFrame, text="Ingrese su nombre", fg="red", font=("Comics Sans MS", 18))
# nos permite ubicar el label en cualquier lugar
mi_label.place(x=100, y=200)
mi_imagen = PhotoImage(file="python3.gif")
label2 = Label(miFrame, image=mi_imagen)
label2.place(x=200, y=200)
# Bucle infinito para permanecer a la escucha de eventos
root.mainloop()
