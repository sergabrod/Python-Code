# -*- coding: utf-8 -*-
# Son errores que ocurren en tiempo de ejecución, no son de sintaxis.
# Manejando errores en tiempo de ejecución


def divide():
    try:
        num1 = float(input("introduzca un número: "))
        num2 = float(input("introduzca otro número: "))
        print("la división es: " + str(num1/num2))
    except ValueError:
        print("El valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        # con finally esta instrucción se ejecuta siempre
        print("cálculo finalizado")


def divide_sin_except():
    try:
        num1 = float(input("introduzca un número: "))
        num2 = float(input("introduzca otro número: "))
        print("la división es: " + str(num1/num2))
    finally:
        # Sin except da error pero esta instrucción se ejecuta siempre
        print("cálculo finalizado")


divide()
divide_sin_except()


