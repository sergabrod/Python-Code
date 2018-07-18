# -*- coding: utf-8 -*-
# utilizando radio button

from tkinter import *

root = Tk()
root.title("Turismo")

playa = IntVar()
montana = IntVar()
turismo = IntVar()


def opciones_viaje():
    opcion_elegida = ""
    if playa.get() == 1:
        opcion_elegida += " Playa"
    if montana.get() == 1:
        opcion_elegida += " Montaña"
    if turismo.get() == 1:
        opcion_elegida += " Turismo Rural"

    if opcion_elegida == "":
        textoFinal.config(text="")
    else:
        textoFinal.config(text="Elegiste: " + opcion_elegida)


foto = PhotoImage(file="viajes.png")
Label(root, image=foto).pack()
frame = Frame(root)
frame.pack()
Label(frame, text="Elige tu destino:", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opciones_viaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opciones_viaje).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismo, onvalue=1, offvalue=0, command=opciones_viaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
