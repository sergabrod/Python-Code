# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

try:
    cursor.execute("""
        CREATE TABLE productos (
            codigo VARCHAR(4) PRIMARY KEY, 
            descripcion VARCHAR(100), 
            precio INTEGER, 
            seccion VARCHAR(20))
            """)
except:
    print("La tabla productos ya existe")

productos = [
    ('P001', 'Camiseta', 5, 'Deportes'),
    ('P002', 'Short', 9, 'Deportes'),
    ('P003', 'Medias', 3, 'Deportes'),
    ('P004', 'Microcomponente', 25, 'Audio'),
    ('P005', 'Parlantes', 59, 'Audio'),
    ('P006', 'Subwoofer', 23, 'Audio'),
]
cursor.executemany("INSERT INTO productos VALUES(?, ?, ?, ?)", productos)

conexion.commit()
conexion.close()
