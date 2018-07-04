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
        self.__gasolina = "no"
        self.__aceite = "no"
        self.__puertas = "no"

    # self hace referencia a la instancia de la clase, this en php, es obligatorio ponerlo como primer parámetro
    def arrancar(self):
        if self.__control_interno():
            self.en_marcha = True
        else:
            self.en_marcha = False

    def detener(self):
        self.en_marcha = False

    def estado(self):
        if self.en_marcha:
            return "El coche está en marcha"
        else:
            return "El coche está detenido"

    def ruedas(self):
        return self.__ruedas

    # Método privado inicia con __
    def __control_interno(self):
        print("realizando chequeo interno...")
        self.__gasolina = "ok"
        self.__aceite = "ok"
        self.__puertas = "cerradas"

        if self.__gasolina == "ok" and self.__aceite == "ok" and self.__puertas == "cerradas":
            return True
        else:
            return False


mi_coche = Coche()
mi_coche.arrancar()
print(mi_coche.estado())
mi_coche.detener()
print(mi_coche.estado())
# print(mi_coche.__control_interno()) No se puede acceder al método interno


print("----------- segundo objeto --------------")
mi_coche2 = Coche()
print(mi_coche2.estado())
