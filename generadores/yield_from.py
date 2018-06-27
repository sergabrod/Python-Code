# -*- coding: utf-8 -*-
# Utilizando yield from
# En Python el asterisco significa que no se sabe qué cantidad de elementos se recibirán
# y que además esos argumentos se recibirán en forma de tupla


def devuelve_ciudades(*ciudades):
    for ciudad in ciudades:
        # for barrio in ciudad:
        #     yield barrio
        yield from ciudad  # se reemplaza el bucle anidado por yield from


ciudades_devueltas = devuelve_ciudades('Capital', 'Goya', 'Mercedes', 'Curuzú')
print(next(ciudades_devueltas))
print("Sigue imprimiendo")
print(next(ciudades_devueltas))
