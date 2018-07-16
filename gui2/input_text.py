# -*- coding: utf-8 -*-
# Trabajando con Tkinter

from tkinter import *

# Creamos la raiz del contenedor TK
root = Tk()
root.title("Inputs con Tkinter")
root.geometry("650x500")
root.resizable(True, True)

# Creo un frame y lo agrego a la raiz (root), antes debemos empaquetarlo
miFrame = Frame(root, width=500, height=400)
miFrame.pack()
# Creo una variable nombre
nombre = StringVar()
# Creamos un grid, que es como una tabla para ubicar elementos
# Creamos el label
# Con el paràmetro sticky alineamos el label segùn puntos cardinales
# padx, pady, nos da el espacio entre el widget y el contenedor
label1 = Label(miFrame, text="Usuario:")
label1.grid(row=1, column=0, sticky="e", padx=5, pady=25)

input1 = Entry(miFrame, textvariable=nombre)
input1.grid(row=1, column=1)
input1.config(fg="red", justify="center")

label2 = Label(miFrame, text="Password:")
label2.grid(row=1, column=2, sticky="e", padx=5, pady=25)

input2 = Entry(miFrame)
input2.grid(row=1, column=3)
input2.config(show="*")

label3 = Label(miFrame, text="Apellido:")
label3.grid(row=2, column=0, sticky="e", padx=5, pady=25)

input3 = Entry(miFrame)
input3.grid(row=2, column=1)

label4 = Label(miFrame, text="Nombre:")
label4.grid(row=2, column=2, sticky="e", padx=5, pady=25)

input4 = Entry(miFrame)
input4.grid(row=2, column=3)

label5 = Label(miFrame, text="Comentario:")
label5.grid(row=3, column=0, sticky="e", padx=5, pady=10)

input6 = Text(miFrame, width=35, height=15)
input6.grid(row=3, column=1)
scrollbar = Scrollbar(miFrame, command=input6.yview)
# Para ubicar el scrollbar a la derecha
scrollbar.grid(row=3, column=2, sticky="nsew")
# setea para que el scroll se desplace con el texto
input6.config(yscrollcommand=scrollbar.set)


def codigoBoton():
    nombre.set("Sergio Gabriel")


botonEnviar = Button(root, text="Guardar", command=codigoBoton)
botonEnviar.pack()

# Bucle infinito para permanecer a la escucha de eventos
root.mainloop()
