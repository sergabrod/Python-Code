# -*- coding: utf-8 -*-
# Serialización de objetos con la biblioteca Pickle

import pickle


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


coche1 = Vehiculo("Ford", "Eco Sport")
coche2 = Vehiculo("Chevrolet", "Tracker")
coche3 = Vehiculo("Renault", "Sandero")
coches = [coche1, coche2, coche3]

archivo = open("objetos_coches.bin", "wb")
pickle.dump(coches, archivo)
archivo.close()
del archivo

# Ahora leemos el archivo generado

archivo_objetos = open("objetos_coches.bin", "rb")
coches = pickle.load(archivo_objetos)
archivo_objetos.close()
for coche in coches:
    coche.estado()



