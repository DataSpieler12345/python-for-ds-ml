# Dictionary
# una lista tiene index y elementos, un diccionario tiene Key para indexar y el valor asociado
# las key son inmutable y únicos 
# Los valores pueden ser inmutable, mutable y duplicados
# cada Key es seguido por un valor y separado by colon

# Creating a dictionary 

movies = {"Thriller": 1982, "Black in Black": 1980, "The Dark Side of the Moon": 1973, "The Bodyguard": 1992}
print(type(movies))
print(movies)
print(len(movies))

# Indexing diccionario

print(movies)
print(movies["Black in Black"])
print(movies["Thriller"])
print(movies["The Dark Side of the Moon"])
print(movies["The Bodyguard"])

# Eliminando Elementos de un diccionario

letras = {"a": 3, "e":6, "i": 2, "o": 7, "u":4}

# opción 1 - pop - elimina el elemento indicado y si no existe devuelve error

letras.pop("a") # elimina la clave a y su valor 
print(letras)

# opción 2 - popitem - elimina el ultimo elemento del diccionario

letras.popitem()
print(letras)

#  opción 3 - del + key - permite borrar el elemento que nosotros indiquemos mediante la llave
del letras["e"]
print(letras)

# opción 4 - clear - para borrar todos los elementos del diccionario
# letras.clear()
# print(letras)
# {}

# opción 5 - del - permite borrar el diccionario entero
# del letras
# print(letras)
# Trace back - Name Error (no existe ya por eso el error)

#checking elements in diccionario

# Usamos diccionario letras arriba definido - buscamos por clave de diccionario
if "a" in letras:
    print("Clave existe")
else:
    print("Clave no existe")

if "j" in letras:
    print("Clave existe")
else:
    print("Clave no existe")

if "i" in letras:
    print("Clave existe")
else:
    print("Clave no existe")

if "o" in letras:
    print("Clave existe")
else:
    print("Clave no existe")

if "u" in letras:
    print("Clave existe")
else:
    print("Clave no existe")

# Accediendo a todas las claves del diccionario letras

llaves = letras.keys()
print(llaves)
print(type(letras))

# New Dic_Testing

dict01 = {"Ben": 45, "Frank": 39, "Patty": 39, "Marlyn": 65, "Clara": "1M"}
print(dict01)
print(len(dict01))
print(type(dict01))

# indexing  Dic 1

print(dict01["Ben"])
print(dict01["Frank"])
print(dict01["Patty"])
print(dict01["Marlyn"])
print(dict01["Clara"])

# Indexing Dic 2

if "Ben" in dict01:
    print("Clave existe")
else:
    print("Clave no existe")

if "Frank" in dict01:
    print("Clave existe")
else:
    print("Clave no existe")

if "Patty" in dict01:
    print("Clave existe")
else:
    print("Clave no existe")

if "Marlyn" in dict01:
    print("Clave existe")
else:
    print("Clave no existe")

if "Clara" in dict01:
    print("Clave existe")
else:
    print("Clave no existe")

print(dict01.keys()) # Regresa todas las llaves del diccionario
print(dict01.values())  # Regresa todos los valores asociados a las llaves del diccionario

# Lab 1 | Consider is the result of the following D.values()?

d = {"a": 0, "b": 1, "c": 2}

print(d.values())
print(d["b"])

# Lab 2 | What is the syntax used to obtain the first element of the tuple: A ("a", "b", "c")

A = ("a", "b", "c")
print(A[0])

# Lab 3 | Consider the following Python dictionary:

dict02 = {"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}

# What is the result of the following operation: Dict["D"]?
print(dict02["D"])


