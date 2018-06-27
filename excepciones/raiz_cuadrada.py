# -*- coding: utf-8 -*-
# Son errores que ocurren en tiempo de ejecución, no son de sintaxis.
# Manejando errores en tiempo de ejecución
# Con raise personalizamos el mensaje de la excepción


import math


def calcula_raiz(numero):
    if numero < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(numero)


numero_ingresado = int(input("Introduce un número: "))
try:
    print(calcula_raiz(numero_ingresado))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("programa terminado")
