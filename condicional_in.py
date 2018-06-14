# -*- coding: utf-8 -*-
# trabajando con condicionales

asignaturas = ('computación gráfica', 'calidad de Software', 'sistemas distribuidos')
print("Asignaturas optativas de la carrera de Sistemas")
print(' - '.join(asignaturas))

asignatura_elegida = input("Ingrese el nombre de la asignatura a cursar: ")

if asignatura_elegida.lower() in asignaturas:
    print("Asignatura elegida: " + asignatura_elegida)
else:
    print("La asignatura no está en la lista")

# Ahora elección por número

for i in range(0, len(asignaturas)):
    print("Opción " + str(i+1) + ": " + asignaturas[i])

asignatura_numero = int(input("Ingrese el número de la asignatura a cursar: "))
if asignatura_numero in range(1, len(asignaturas) + 1):
    print("La asignatura elegida es: " + asignaturas[asignatura_numero - 1])
else:
    print("La asignatura no está en la lista")


