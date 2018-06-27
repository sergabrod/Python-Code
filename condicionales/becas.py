# -*- coding: utf-8 -*-
# trabajando con condicionales

print("Programa de becas 2018")
distancia_escuela = int(input("Ingrese su distancia a la Escuela en Km: "))
salario_familiar = int(input("Ingrese su salario: "))
cantidad_hnos = int(input("Ingrese el número de hermanos: "))

print("Distancia a escuela: " + str(distancia_escuela))
print("Salario familiar: " + str(salario_familiar))
print("Cantidad de hermanos: " + str(cantidad_hnos))

if distancia_escuela > 40 and cantidad_hnos > 2 or salario_familiar <= 20000:
    print("Tiene derecho a beca")
else:
    print("No tiene derecho a beca")
