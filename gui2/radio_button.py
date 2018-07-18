# -*- coding: utf-8 -*-
# utilizando radio button

from tkinter import *

root = Tk()

opcion = IntVar()


def imprimir():
    if opcion.get() == 1:
        label2.config(text="has elegido Masculino")
    elif opcion.get() == 2:
        label2.config(text="has elegido Femenino")
    else:
        label2.config(text="has elegido Otro")


Label(root, text="Género:").pack()
Radiobutton(root, text="Masculino", variable=opcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=opcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otro", variable=opcion, value=3, command=imprimir).pack()
label2 = Label(root)
label2.pack()

root.mainloop()
