# -*- coding: utf-8 -*-
# Trabajando con archivos y el módulo io
from io import open

"""Abrimos el archivo en modo lectura"""
archivo_texto = open("archivo.txt", "r")
# texto = archivo_texto.read()
# Devuelve una lista donde cada renglón es un elemento
lineas_texto = archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto[0])

"""Abrimos el archivo en modo de agregar"""
archivo_texto = open("archivo.txt", "a")
archivo_texto.write("\nAquí agregamos una línea al texto")
archivo_texto.close()




