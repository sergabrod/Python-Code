# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM productos WHERE seccion = 'Audio'")
productos = cursor.fetchall()
print(productos)

cursor.execute("UPDATE productos set precio=45 WHERE id = 4")

cursor.execute("SELECT * FROM productos WHERE id = 4")
productos = cursor.fetchall()
print(productos)

conexion.commit()
conexion.close()
