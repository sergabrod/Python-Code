# -*- coding: utf-8 -*-
# Trabajando con herencia


class vehiculo(object):
    "Clase que representa a un Vehìculo"
    def __init__(self, marca, modelo):
        "Constructor de Vehìculo"
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


class moto(vehiculo):
    def __init__(self, marca, modelo):
        vehiculo.__init__(self, marca, modelo)


moto1 = moto("Honda", "cbr")
moto1.estado()

