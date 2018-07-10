# -*- coding: utf-8 -*-
# Trabajando con archivos y el módulo io
from io import open

"""Abrimos el archivo en modo lectura"""
archivo_texto = open("archivo.txt", "r")

# Una vez leído el archivo, el puntero queda al final del mismo
print("Leo el archivo con el primer read: ")
print(archivo_texto.read())
# Con seek lo volvemos a la posición que deseemos
print("Posiciono el archivo con el seek a 25: ")
archivo_texto.seek(25)
# Con read le podemos decir hasta que caracter leer el archivo
print("Leo el archivo hasta la posición 10: ")
print(archivo_texto.read(10))

# Posiciono el puntero en la mitad del archivo
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())
archivo_texto.close()
