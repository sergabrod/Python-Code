# -*- coding: utf-8 -*-
# Trabajando con Polimorfismo


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


class Coche(object):
    def desplazamiento(self):
        print("se desplaza utilizando cuatro ruedas")


class Moto(object):
    def desplazamiento(self):
        print("se desplaza utilizando dos ruedas")


class Camion(object):
    def desplazamiento(self):
        print("me desplazo utilizando seis ruedas")


unaMoto = Moto()
unCoche = Coche()
unCamion = Camion()

desplazamientoVehiculo(unaMoto)
desplazamientoVehiculo(unCoche)
desplazamientoVehiculo(unCamion)


