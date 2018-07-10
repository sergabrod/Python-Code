# -*- coding: utf-8 -*-
# Guardar en archivos los objetos persona

import pickle
from persona import Persona
from lista_persona import ListaPersona


persona1 = Persona("Juan", "Masculino", 25)
persona2 = Persona("Pedro", "Masculino", 35)
persona3 = Persona("Maria", "Femenino", 18)
persona4 = Persona("Josefa", "Femenino", 40)
persona5 = Persona("Pepe", "Masculino", 53)

lista = ListaPersona()
lista.agregar_persona(persona1)
lista.agregar_persona(persona2)
lista.agregar_persona(persona3)
lista.agregar_persona(persona4)
lista.agregar_persona(persona5)
lista.mostrar_personas_en_archivo()



