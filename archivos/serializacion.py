# -*- coding: utf-8 -*-
# Trabajando serialización con la biblioteca Pickle

import pickle
#from io import open

lista_nombres = ["Juan", "Pedro", "Maria", "José"]
# abrimos el archivo para escritura binaria
archivo_binario = open("listado.bin", "wb")
pickle.dump(lista_nombres, archivo_binario)
archivo_binario.close()

# Ahora lo leemos
archivo = open("listado.bin", "rb")
lista = pickle.load(archivo)
print(lista)


