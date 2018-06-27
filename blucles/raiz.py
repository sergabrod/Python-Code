# -*- coding: utf-8 -*-
# Bucles while: Raiz cuadrada

import math

numero = int(input("Introduzca un número: "))
intentos = 0
while numero < 0:
    print("No se puede hallar la raiz cuadrada de un número negativo")
    intentos += 1

    if intentos == 2:
        print("Ya intentaste demasiadas veces")
        break

    numero = int(input("Introduzca un número: "))

if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es " + str(solucion))
