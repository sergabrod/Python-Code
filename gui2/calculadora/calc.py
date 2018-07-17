# -*- coding: utf-8 -*-
# Calculadora con Tkinter

from tkinter import *

# Creamos la raiz del contenedor TK
root = Tk()
root.title("Calculadora con Tkinter")
root.resizable(True, True)

# Creo un frame principal y lo agrego a la raiz (root), antes debemos empaquetarlo
frame_principal = Frame(root, width=300, height=350)
frame_principal.pack()

# ----------- Pantalla principal de la calculadora----------------
pantalla = Entry(frame_principal)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# ----------- Fila 1 de la calculadora ---------------------------
boton7 = Button(frame_principal, text="7", width="3")
boton7.grid(row=2, column=1)
boton8 = Button(frame_principal, text="8", width="3")
boton8.grid(row=2, column=2)
boton9 = Button(frame_principal, text="9", width="3")
boton9.grid(row=2, column=3)
botonDiv = Button(frame_principal, text="/", width="3")
botonDiv.grid(row=2, column=4)

# ----------- Fila 2 de la calculadora ---------------------------
boton4 = Button(frame_principal, text="4", width="3")
boton4.grid(row=3, column=1)
boton5 = Button(frame_principal, text="5", width="3")
boton5.grid(row=3, column=2)
boton6 = Button(frame_principal, text="6", width="3")
boton6.grid(row=3, column=3)
botonMult = Button(frame_principal, text="x", width="3")
botonMult.grid(row=3, column=4)

# ----------- Fila 3 de la calculadora ---------------------------
boton1 = Button(frame_principal, text="1", width="3")
boton1.grid(row=4, column=1)
boton2 = Button(frame_principal, text="2", width="3")
boton2.grid(row=4, column=2)
boton3 = Button(frame_principal, text="3", width="3")
boton3.grid(row=4, column=3)
botonRest = Button(frame_principal, text="-", width="3")
botonRest.grid(row=4, column=4)

# ----------- Fila 4 de la calculadora ---------------------------
boton0 = Button(frame_principal, text="0", width="3")
boton0.grid(row=5, column=1)
botonComa = Button(frame_principal, text=",", width="3")
botonComa.grid(row=5, column=2)
botonIgual = Button(frame_principal, text="=", width="3")
botonIgual.grid(row=5, column=3)
botonMas = Button(frame_principal, text="+", width="3")
botonMas.grid(row=5, column=4)


root.mainloop()

