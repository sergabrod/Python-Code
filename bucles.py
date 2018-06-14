# -*- coding: utf-8 -*-
# trabajando con bucles

for i in ["primavera", "verano", "otoño", "invierno"]:
    # que no haga salto de línea
    print(i, end=" - ")

email_ingresado = input("Ingrese su email: ")

email = False
for i in email_ingresado:
    if i == '@':
        email = True
        break

if email:
    print(email_ingresado + " es un email")
else:
    print(email_ingresado + " no es un email")


if '@' and '.' in email_ingresado:
    print("es un mail")
else:
    print("no es un email")
