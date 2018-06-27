# -*- coding: utf-8 -*-
# Son errores que ocurren en tiempo de ejecución, no son de sintaxis.
# Manejando errores en tiempo de ejecución


def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "operación errónea"


while True:
    try:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        break
    except ValueError:
        print("los valores ingresados no son correctos, inténtelo de nuevo")

print(divide(num1, num2))
print("La operación ha sido ejecutada")
