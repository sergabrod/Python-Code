# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

try:
    cursor.execute("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            descripcion VARCHAR(100) UNIQUE, 
            precio INTEGER, 
            seccion VARCHAR(20))
            """)
except:
    print("La tabla productos ya existe")

productos = [
    ('Camiseta', 5, 'Deportes'),
    ('Short', 9, 'Deportes'),
    ('Medias', 3, 'Deportes'),
    ('Microcomponente', 25, 'Audio'),
    ('Parlantes', 59, 'Audio'),
    ('Subwoofer', 23, 'Audio'),
]
cursor.executemany("INSERT INTO productos VALUES(NULL, ?, ?, ?)", productos)

conexion.commit()
conexion.close()
