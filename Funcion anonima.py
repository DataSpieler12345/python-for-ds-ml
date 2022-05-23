# Funcion Map / Lambda / funcion anonima / devuelve una lista
lista = [23,56,7,2,6,9,18,21,75,65]
print(list(map((lambda valor:valor * valor), lista)))

#Funcion Filter / devuelve una lista
print(list(filter((lambda valor:valor%2 ==0),lista)))

#Funcion reduce / devuelve un valor 
import functools
print(str(functools.reduce((lambda x,resultado:x+resultado),lista)))
