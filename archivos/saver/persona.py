# -*- coding: utf-8 -*-
# Clase Persona


class Persona(object):
    """Clase Persona"""
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        # print("Se ha creado una persona con el nombre ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
