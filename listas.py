# Listas en Python
# Son elementos mutables

servidores = ['server1', 'server2', 'server3', 'server-web']
print (servidores[0])
servidores[0] = 'server-db'
print(servidores)

# Posición de i hasta j (no inclusive)
print(servidores[1:3])

# Posición de 2 hasta el final
print(servidores[2:])
print(servidores[-2])
print('server2' in servidores)

# Agrega un elemento al final de la lista
servidores.append('servidor-bd')

# Agrega un elemento en una posición
servidores.insert(3, 'server4')
print(servidores)

# Agrega varios elementos a la lista
servidores.extend(['server5', 'server6'])
print(servidores)

# Devuelve en que indice está un elemento
print(servidores.index('server5'))

# Eliminar un elemento
servidores.remove('server5')
print(servidores)

# Elimina el ultimo elemento de una lista
servidores.pop()
print(servidores)

# Multiplicar una lista
print(servidores * 3)
