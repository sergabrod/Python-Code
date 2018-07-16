# -*- coding: utf-8 -*-
# Trabajando con SQLite


import sqlite3

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor()

productos = [
    ('Camiseta', 5, 'Deportes'),
    ('Short', 9, 'Deportes'),
    ('Medias', 3, 'Deportes'),
    ('Microcomponente', 25, 'Audio'),
    ('Parlantes', 59, 'Audio'),
    ('Subwoofer', 23, 'Audio'),
]
cursor.executemany("INSERT INTO productos VALUES(?, ?, ?)", productos)
conexion.commit()
conexion.close()
