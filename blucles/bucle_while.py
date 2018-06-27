# -*- coding: utf-8 -*-
# Bucles while

i = 1
while i <= 10:
    print(f"Esta es la iteración número {str(i)}")
    i += 1

edad = int(input("Introduce la edad, por favor: "))

while not 0 < edad < 120:
    print("La edad no es correcta")
    edad = int(input("Introduce la edad, por favor: "))

print("Su edad es " + str(edad))

