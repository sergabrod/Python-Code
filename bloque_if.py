# -*- coding: utf-8 -*-
# trabajando con condicionales


def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "desaprobado"

    return valoracion


# Ingresamos por teclado
print("Evaluación de Notas")
nota = input("Ingrese su nota: ")
print(evaluacion(int(nota)))


