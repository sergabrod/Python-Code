# Las tuplas son elementos inmutables en Python
# No permiten añadir, eliminar, ni mover elementos
# no permiten búsquedas, sí comprobar si un elemento se encuentra en la tupla
# Son más rápidas, menos espacio, formatean string.
# Se pueden utilizar como claves de un diccionario (las listas no)

usuarios = ('usuario1', 'usuario2', 'usuario3', 'usuario4', 7, 'usuario1')
print(usuarios)
print(usuarios[2])

# Para convertir una tupla en una lista
lista_usuarios = list(usuarios)
print(lista_usuarios)

# Para convertir una lista en una tupla
usuarios = tuple(lista_usuarios)
print(usuarios)

# Para verificar si un elemento existe en la tupla
print('usuario3' in usuarios)

# Averiguar cuántos elementos se encuentran en la tupla
print(usuarios.count('usuario1'))

# Averiguar la longitud de la tupla
print(len(usuarios))

# Una tupla unitaria lleva una coma al final del único elemento
usuario = ("Sergio",)
print(usuario)

# Asignar una tupla a variables (desempaquetado de tuplas)
registro = ('Sergio', 5, 6, 2018)
nombre, dia, mes, anio = registro
print("Su nombre es " + nombre + ", hoy es " + str(dia) + '/' + str(mes) + '/' + str(anio))

