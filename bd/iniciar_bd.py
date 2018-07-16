# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

try:
    cursor.execute("CREATE TABLE productos (descripcion VARCHAR(100), precio INTEGER, seccion VARCHAR(20))")
except:
    print("La tabla productos ya existe")

cursor.execute("INSERT INTO productos VALUES ('Notebook HP', 15, 'Computaciòn')")
cursor.execute("INSERT INTO productos VALUES ('Celular Iphone', 30, 'Computaciòn')")
cursor.execute("INSERT INTO productos VALUES ('Lavarropas Samsung', 120, 'Hogar')")
cursor.execute("INSERT INTO productos VALUES ('Cocina Longvie', 145, 'Hogar')")
cursor.execute("INSERT INTO productos VALUES ('Calefactor', 13, 'Hogar')")
conexion.commit()
conexion.close()
