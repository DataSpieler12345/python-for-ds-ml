#Damos valor a variable
precio = 225
cantidad = 3

#Calculamos total
total = precio * cantidad
#Mostrando resultado
print('El precio total es de:', total)
print(type(precio))
print(type(cantidad))
print(type(total))

#Borrando variable 
del precio
print(cantidad)

#Asignand otros valores
precio = 25
cantidad = 21

#Calculamos el total
total = precio * cantidad

#mostrar resultado
print('El precio total es de: ', total)

#VARIABLES CONSTANTES EN MAYUSCULA - quedan fijas una vez que se inicializan. 
PASSWORD = '123456'
print(PASSWORD)

#Asignar varios valores a la vez 
a,b,c,d = 1,4,'nombre', True
print(a)
print(b)
print(c)
print(d)

#Asignar el mismo valor a varias variables
x = yy = z = 68
print(x)
print(yy)
print(z)
