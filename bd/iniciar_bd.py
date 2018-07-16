# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

try:
    cursor.execute("CREATE TABLE productos (descripcion VARCHAR(100), precio INTEGER, seccion VARCHAR(20))")
except:
    print("La tabla productos ya existe")

cursor.execute("INSERT INTO productos VALUES ('Notebook HP', 15, 'Tecnologìa'")
cursor.execute("INSERT INTO productos VALUES ('Notebook HP', 15, 'Tecnologìa'")
cursor.execute("INSERT INTO productos VALUES ('Notebook HP', 15, 'Tecnologìa'")
cursor.execute("INSERT INTO productos VALUES ('Notebook HP', 15, 'Tecnologìa'")

conexion.close()
