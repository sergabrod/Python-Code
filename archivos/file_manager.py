# -*- coding: utf-8 -*-
# Trabajando con archivos y el módulo io
from io import open

"""Abrimos el archivo en modo escritura"""
archivo_texto = open("archivo.txt", "w")

frase = "Hoy es un muy buen día para estudiar Python.\nBuen Martes."
archivo_texto.write(frase)
archivo_texto.close()

