# -*- coding: utf-8 -*-
# trabajando con condicionales


def mayor_de_edad(edad):

    if edad < 18:
        print("Usted es menor de edad")
    elif edad == 18:
        print("Usted tiene 18 años")
    else:
        print("Usted es mayor de edad")


# Ingresamos por teclado
print("Control de mayoría de edad")
edad = input("Ingrese su edad: ")
print(mayor_de_edad(int(edad)))
