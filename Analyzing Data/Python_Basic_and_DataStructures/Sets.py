# Sets
# Sets are type of collection 
# this means that like lists and tuples you can input different Python types
# Unlike lists and tuples they are unordered 
# This means sets do not record element position 
# Sets only have unique elements
# this means there is only one of a particular element in a set


# Creating a Set
Set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(type(Set1))
print(Set1)
print(len(Set1)) # "rock" 3 times    

# Convert a list to a set by using the function set, called type-casting

album_list = ["Michael Jackson","Thriller", "Thriller", 1982]
print(type(album_list))
print(album_list)
print(len(album_list)) # No toma en cuenta los duplicados en la lista

album_set = set(album_list) # list converted to a set
print(type(album_set))
print(album_set)
print(len(album_set)) # "Thriller" 2 veces duplicado

# Set Operation

A = {"Thriller", "Black in Black", "AC/DC"}

A.add("Britney Spears") # agregamos a Britney Spears al Set previo definido
print(A)

# Removing Britney Spears del Set

A.remove("Britney Spears") # Britney a sido removida del Set
print(A)

# Checking si un elemento esta en el set, devuelve un verdadero o falso
if "AC/DC" in A:
    print("Si existe el elemento 'AC/DC'")
else:
    print("Elemento no pertenece al conjunto de datos")

if "Hanson" in A:
    print("Si existe el elemento 'Hanson'")
else:
    print("Elemento no pertenece al conjunto de datos, elemento necesita ser agregado al set de datos")

# Mathematical set operations

A1 = {"Thriller", "Comedy", "Drama"}
print(type(A1))
print(A1)   
print(len(A1))

# union of two set A & A1. Se unen los elementos de A y A1 consiste en todos los elementos de A y todos los elementos de B de tal manera que ningún elemento se repite
print("A U A1 :", A.union(A1))

# Adding a A2 data set to A U A1 set

A2 = ("Nora Johns",  "Beatles", "Cuneta son Machine" )
print("A U A1 U A2:", A.union(A1, A2))

# Muestra los elementos en común entre sets por eso devuelve solo Thriller. Si no hay en común elementos devuelve error la consola, A1 & A2 por ejemplo no tienen elementos que los una. 
set_test = A & A1
print(set_test)

# Preguntamos si A es un sub
A.issubset(A1)
print(A)

# Lab 1 | What is the resulto of the following lines of code

S = {"A", "B", "C"}
U = {"A", "Z", "C"}

print("U U S :", U.union(S))

# Lab 2 | What is the intersection of set s und u?

abc = S & U
print(abc)




