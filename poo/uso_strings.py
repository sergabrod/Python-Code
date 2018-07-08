# -*- coding: utf-8 -*-
# Trabajando con Strings


nombre_usuario = input("Ingrese su nombre: ")
print("El nombre en mayùsculas es: ", nombre_usuario.upper())
print("El nombre en minùsculas es: ", nombre_usuario.lower())
print("Con la primer letra en mayùscula es: ", nombre_usuario.capitalize())

edad = input("Introduzca la edad: ")
while not edad.isdigit():
    edad = input("Debe ingresar un valor numèrico: ")

print(edad.isdigit())

if int(edad) < 18:
    print("No puedes ingresar")
else:
    print("Bienvenido al site")


