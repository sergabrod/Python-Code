# -*- coding: utf-8 -*-
# trabajando con condicionales

salario_presidente = int(input("Introduzca salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduzca salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduzca salario del jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduzca salario del administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo esta ok")
else:
    print("Algo funciona mal en la empresa")
