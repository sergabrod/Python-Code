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
    "Clase moto hereda de Vehìculo"
    wheely = "no hace wheely"

    def __init__(self, marca, modelo):
        vehiculo.__init__(self, marca, modelo)

    def hace_wheely(self):
        self.wheely = "haciendo wheely"

    def estado(self):
        vehiculo.estado(self)
        print("Wheely ", self.wheely)


class furgoneta(vehiculo):
    "Clase furgoneta"
    cargado = ""

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta està cargada"
        else:
            return "La furgoneta no està cargada"


class MovilElectrico(object):
    def __init__(self):
        self.autonomia = 100
        self.cargando = False

    def cargar_energia(self):
        self.cargando = True

