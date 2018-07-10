# -*- coding: utf-8 -*-
# Trabajando con archivos y el módulo io
from io import open

"""Abrimos el archivo en modo lectura y escritura"""
archivo_texto = open("archivo.txt", "r+")
archivo_texto.write("Comienza de nuevo el texto y sobreescribe")
# Al abrir el modo lectura y escritura imprime como una lista
# print(archivo_texto readlines())

# Agregamos una linea reemplazándola por código
lista_texto = archivo_texto.readlines()
lista_texto[1] = "esta línea ha sido agregada desde afuera\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()



