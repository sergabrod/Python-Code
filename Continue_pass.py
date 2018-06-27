# -*- coding: utf-8 -*-
# Bucles while: continue y pass
# pass devuelve null en un bucle
# continue salta a la siguiente línea


for letra in "Python":
    if letra == "h":
        continue
    print("viendo la letra " + letra)

# Cuento sólo los caracteres y no los espacios
texto = "Programación en Python"
contador = 0
for letra in texto:
    if letra == " ":
        continue
    contador += 1
print("cantidad de letras es " + str(contador))
print(len(texto))

# pass se puede detener el loop infinito con control+c
# sirve para dejar en null una parte del código

while True:
    pass
