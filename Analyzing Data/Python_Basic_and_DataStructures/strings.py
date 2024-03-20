#Indexing con Strings

name = "Michael Jackson"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[12])
print(name[13])
print(name[14])

# Con nominación negativa

print(name[-15])
print(name[-14])
print(name[-13])
print(name[-12])
print(name[-11])
print(name[-10])
print(name[-9])
print(name[-8])
print(name[-7])
print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

# Strings Slicing 

print(name[0:4])
print(name[8:12])

print(name[::2])
print(name[0:5:2])

# len command

print(len("Michael Jackson"))

# Combinar o concatenar Strings

actualizando = name +" is the best"
print(actualizando)

# Tuples

multiplicación = name * 3
print(multiplicación)

# Strings escape sequences

print("Michael Jackson\n is the best")
print(" Michael Jackson \t is the best")
print(r"Michael Jackson \ is the best")

# String Method

A = "Thriller is the sixth studio album"
print(A.upper()) # Regresa el string en mayúscula 
print(A.lower()) # Regresa el string en minúscula 
print(A.isupper()) # Para check si esta en mayúscula = Falso
print(A.islower()) # Para check si esta en minúscula = Falso

# Method Replace Strings

string = 'Michael Jackson is the best'
new_string = string.replace("Michael", "Janet")

print(string)
print(new_string)

# String Stride (La variable name esta creada arriba al inicio del script)

print(name.find("el")) # Devuelve el primer valor de la cadena de texto buscada. 
print(name.find("Jack"))
print(name.find("&*D"))

# Lab 1
numbers = "0123456"

print(numbers[::3])
print('even values',numbers[::2])
print(numbers[::6])

# Lab 2
numero = "0123456"
print(numero.find("1"))

#Lab 3
print(3 + (2*2))

# Lab 4
nombre = "Pizz"
print(nombre[0:2])

# Lab 5
var1 = "01234567"
print(var1[::2])

# Lab 6
print('1'+'2')

# Lab 7
myvar = "hello"
print(myvar.upper())





