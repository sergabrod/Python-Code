# -*- coding: utf-8 -*-
# Trabajando con clases en Python


class Coche():
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False

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


mi_coche = Coche()
print("El largo del coche es:", mi_coche.largo_chasis)
print("El ancho del coche es:", mi_coche.ancho_chasis)
print("El coche tiene", mi_coche.ruedas, "ruedas")

mi_coche.arrancar()
print(mi_coche.estado())
mi_coche.detener()
print(mi_coche.estado())

