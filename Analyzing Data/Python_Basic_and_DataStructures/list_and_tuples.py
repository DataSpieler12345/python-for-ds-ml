# Tuples
# Tuples are an ordered sequence 
# Tuples are written as comma-separated elements within parentheses 
# Tuples are inmutables

ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)

# Tuples are inmutables

ratings1 = ratings
print(ratings1) 
print(type(ratings1)) 

# Para editar un tuples best practices crear uno  nuevo. 
ratingsSorted = sorted(ratings)
print(ratingsSorted)
print(type(ratingsSorted))


# tipos = str ('disco'), int (10), float (1.2)

tuple1 = ('disco', 10, 1.2)
print(type(tuple1))

# indexing tuples

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# negative indexing

print(tuple1[-3])
print(tuple1[-2])
print(tuple1[-1])

# concatenando y combinando tuples

tuple2 = tuple1 + ("hard rock", 10)
print(type(tuple2))
print(tuple2)

# Slicing tuples

print(tuple2[0:3])
print(tuple2[1:4])
print(tuple2[2:5])
print(tuple2[0:6])
print(tuple2[1:7])
print(tuple2[2:8])
print(tuple2[0:9])
print(tuple2[1:10])
print(tuple2[2:11])
print(tuple2[3:5]) #mas largo que el set de datos.

# size del tuple con comando len

print(len(("disco", 10, 1.2, "hard rock", 10))) # respuesta es 5 porque tiene 5 elementos

# Tuples Nesting significa que un tuple puede contener internamente otro/s tuple/s

nt = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
print(nt)
print(type(nt))
print(len(nt))

# Indexing Tuples 

print(nt[0])
print(nt[0:1])
print(nt[1])
print(nt[2])
print(nt[2:1])
print(nt[2][1])
print(nt[2][1][0])
print(nt[2][1][1])
print(nt[2][1][2])
print(nt[2][1][3])
print(nt[2][0])
print(nt[2][0][0])
print(nt[2][0][1])
print(nt[2][0][2])
print(nt[3])
print(nt[3][0])
print(nt[3][1]) 
print(nt[4])
print(nt[4][0])
print(nt[4][1])
print(nt[4][1][0])
print(nt[4][1][1])

# List
# Lists are also ordered sequences
# Lists are mutables
# Lists can contain str, float, int, nested_list, we also add tuples in other data structure

list1 = ["Michael Jackson", 10.1, 1982, [1,2], ('A', 1)]
print(list1)
print(len(list1))
print(list1[0])
print(list1[0][0])
print(list1[0][1])
print(list1[0][2])
print(list1[0][3])
print(list1[0][4])
print(list1[0][5])
print(list1[0][6])
print(list1[0][7])
print(list1[0][8])
print(list1[0][9])
print(list1[0][10])
print(list1[0][11])
print(list1[0][12])
print(list1[0][13])
print(list1[0][14])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[3][0])
print(list1[3][1])
print(list1[4])
print(list1[4][0])
print(list1[4][1])

# Negative Indexing
print(list1[-3])
print(list1[-2])
print(list1[-1])

# List Slicing 

new_list = ["Michael Jackson", 10.1, 1982, "MJ, 1"]
print(new_list)
print(type(new_list))
print(len(new_list))

 # 5 sale del rango mayor de la lista, elige el ultimo valor de la cadena 
print(new_list[0])
print(new_list[1])
print(new_list[2])
print(new_list[3])
print(new_list[3][0])
print(new_list[3][1])
print(new_list[3][2])
print(new_list[3][3])
print(new_list[3][4]) # ultimo valor 

# Concatenando lists y combinando

new_list1 = ["Michael Jackson", 10.1, 1982]
new_list_updated = new_list1 + ["pop", 10]
print(new_list_updated)

# adding content to the list
new_list_updated.extend(["salsa", 10])
print(new_list_updated)

# append command agrega como un elemento mas a la lista
new_list_updated.append(["merengue", 10])
new_list_updated.append(["A"])
new_list_updated.append(["disco",10, 1.2])
print(len(new_list_updated))
print(new_list_updated)

# splitting 

print("A", "B", "C", "D".split(",")) # El resultado es una lista

# Aliasing 

A = ["hard rock", 10, 1.2]
B = A
print(B[0])
print(B[1])
print(B[2])
A[0] = "disco"
print(A[0])
print(B) # Afecta a los valores de B porque ser = A / referencia

# Lab 1 Tuple

A = (0, 1 , 2 , 3)
print(A[0])
print(A[1])
print(A[2])
print(A[3]) # Correcta
print(A[-1]) # Correcta

# Lab 2 List

Z = ["a", "b", "c"]
print(Z[1:])    