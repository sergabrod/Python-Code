# -*- coding: utf-8 -*-
# Trabajando con herencia


class Persona(object):
    """Clase Persona"""

    def __init__(self, nombre, edad, domicilio):
        self.nombre = nombre
        self.edad = edad
        self.domicilio = domicilio

    def __str__(self):
        return "Nombre: " + self.nombre + ", Edad: " + str(self.edad) + ", Domicilio: " + self.domicilio


class Empleado(Persona):
    """ Clase Empleado """

    def __init__(self, nombre, edad, domicilio, salario, antiguedad):
        super().__init__(nombre, edad, domicilio)
        self.salario = salario
        self.antiguedad = antiguedad

    def __str__(self):
        return "Nombre: " + self.nombre + ", Edad: " + str(self.edad) + ", Domicilio: " + self.domicilio \
               + ", Salario: $" + str(self.salario) + ", Antiguedad: " + str(self.antiguedad)


antonio = Persona("Antonio", 55, "San Martin 33")
print(antonio)

pepe = Empleado("Pepe", 40, "Jujuy 78", 20000, 5)
print(pepe)

print(isinstance(antonio, Empleado))
print(isinstance(antonio, Persona))

print(isinstance(pepe, Empleado))
print(isinstance(pepe, Persona))

