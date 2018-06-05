# Las tuplas son elementos inmutables en Python
# No permiten añadir, eliminar, ni mover elementos
# no permiten búsquedas, sí comprobar si un elemento se encuentra en la tupla
# Son más rápidas, menos espacio, formatean string.
# Se pueden utilizar como claves de un diccionario (las listas no)

usuarios = ('usuario1', 'usuario2', 'usuario3', 'usuario4', 7)
print(usuarios)
print(usuarios[2])

# Para convertir una tupla en una lista

lista_usuarios = list(usuarios)
print(lista_usuarios)