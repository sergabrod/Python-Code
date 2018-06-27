# -*- coding: utf-8 -*-
# Diccionarios

paises = {'Alemania': 'Berlín', 'Francia': 'París', 'Inglaterra': 'Londres', 'España': 'Madrid'}

for pais, capital in paises.items():
    print("La capital de " + pais + " es " + capital)

paises['Italia'] = 'Roma'
