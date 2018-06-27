# -*- coding: utf-8 -*-
# Genera pares

# Utilizando funciones


def generador_pares(limite):

    num = 1
    lista = []

    while num <= limite:
        lista.append(num * 2)
        num += 1

    return lista


print(generador_pares(5))

# Utilizando generadores
# Devuelve un iterable, es más eficiente


def generador_pares_generador(limite):

    num = 1
    while num <= limite:
        yield num * 2
        num += 1


devuelve_pares = generador_pares_generador(5)

# Entre cada llamada el generador entra en estado de suspensión
# El generador no crea la lista completa sino a medida que se lo llama
# por lo cual es más eficiente
print(next(devuelve_pares))
print("Aca puede ir más código")
print(next(devuelve_pares))
print("Aca puede ir más código")
print(next(devuelve_pares))
