# -*- coding: utf-8 -*-
# trabajando con bucles range

for i in range(5, 50, 3):
    print(f"valor de la variable {i}")

email_valido = False
email = input("Introduzca su email")

for i in range(len(email)):
    if email[i] == '@':
        email_valido = True

if email_valido:
    print(email + " es un email")
else:
    print(email + " no es un email")
