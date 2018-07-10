# -*- coding: utf-8 -*-
# Serialización de objetos con la biblioteca Pickle

import pickle


# Si no definimos la clase, la lectura de la serialización falla
class Vehiculo(object):
    """Clase que representa a un Vehìculo"""
    def __init__(self, marca, modelo):
        """Constructor de Vehìculo"""
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
            self.en_marcha = True

    def acelerar(self):
            self.acelera = True

    def frenar(self):
            self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.en_marcha, "\nAcelera: ",
              self.acelera, "\nFrena: ", self.frena)

# Ahora leemos el archivo generado
archivo_objetos = open("objetos_coches.bin", "rb")
coches = pickle.load(archivo_objetos)
archivo_objetos.close()
for coche in coches:
    coche.estado()