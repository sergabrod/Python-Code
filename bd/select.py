# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print("Producto:", producto[0], " Precio: $", producto[1], " Categorìa:", producto[2])

conexion.close()

