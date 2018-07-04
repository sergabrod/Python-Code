# -*- coding: utf-8 -*-
# Trabajando con clases en Python


class Coche():

    # Constructor
    def __init__(self):
        self.largo_chasis = 250
        self.ancho_chasis = 120
        # hacemos privada la propiedad rueda
        self.__ruedas = 4
        self.en_marcha = False

    # self hace referencia a la instancia de la clase, this en php, es obligatorio ponerlo como primer parámetro
    def arrancar(self):
        self.en_marcha = True

    def detener(self):
        self.en_marcha = False

    def estado(self):
        if self.en_marcha:
            return "El coche está en marcha"
        else:
            return "El coche está detenido"

    def ruedas(self):
        return self.__ruedas


mi_coche = Coche()
print("El largo del coche es:", mi_coche.largo_chasis)
print("El ancho del coche es:", mi_coche.ancho_chasis)
print("El coche tiene", mi_coche.ruedas(), "ruedas")

mi_coche.arrancar()
print(mi_coche.estado())
mi_coche.detener()
print(mi_coche.estado())

print("----------- segundo objeto --------------")
mi_coche2 = Coche()
mi_coche2.largo_chasis = 230
mi_coche2.ancho_chasis = 100
# Aca no está asignando a la propiedad rueda sino a una variable diferente
mi_coche2.__ruedas = 5

print("El largo del coche es:", mi_coche2.largo_chasis)
print("El ancho del coche es:", mi_coche2.ancho_chasis)
print("El coche tiene", mi_coche2.ruedas(), "ruedas")
print(mi_coche2.estado())
