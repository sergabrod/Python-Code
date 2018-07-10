# -*- coding: utf-8 -*-
# Clase ListaPersona
import pickle


class ListaPersona(object):
    """Clase ListaPersona"""
    personas = []

    def __init__(self):
        lista_personas = open("archivo_personas.bin", "ab+")
        lista_personas.seek(0)
        # se cargan las personas del archivo y se las muestra
        # colocamos el puntero al inicio del archivo
        try:
            self.personas = pickle.load(lista_personas)
            print("se cargaron {} personas del archivo externo: " . format(len(self.personas)))
        except:
            print("El archivo está vacío")
        finally:
            lista_personas.close()
            del lista_personas

    def agregar_persona(self, persona):
        self.personas.append(persona)
        self.guardar_persona()

    def mostrar_personas(self):
        for persona in self.personas:
            print(persona)

    def guardar_persona(self):
        lista_personas = open("archivo_personas.bin", "wb")
        pickle.dump(self.personas, lista_personas)
        lista_personas.close()
        del lista_personas

    def mostrar_personas_en_archivo(self):
        print("Las personas en el archivo son: ")
        for persona in self.personas:
            print(persona)



