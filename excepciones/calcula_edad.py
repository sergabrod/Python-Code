# -*- coding: utf-8 -*-
# Son errores que ocurren en tiempo de ejecución, no son de sintaxis.
# Manejando errores en tiempo de ejecución
# Con raise personalizamos el mensaje de la excepción


def evalua_edad(edad):

    if edad < 0:
        # con raise estamos lanzando la excepción pero no estamos capturándola
        raise ZeroDivisionError("No se permiten edades negativas")
    if edad < 20:
        return "sos muy joven"
    elif edad < 40:
        return "sos joven"
    elif edad < 65:
        return "sos maduro"
    elif edad < 100:
        return "cuidate"


print(evalua_edad(-18))
