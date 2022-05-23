print('Bienvenidos a mi primer programa con Python')
print('Tipo entero')
print(type(23))
print('Tipo decimal')
print(type(12.32))
print('Tipo cadena')
print(type('Saludo'))
print('Tipo booleano')
print(type(False))
#comentarios a nivel interno para leer mejor el codigo a nivel personal y bien a nivel de equipo 

# Ejemplos con las cadenas 
print('Hola, '+' amigos!!!')
print('Saludo' * 4)
#variable = 'cadena en variable'
variable = 'Sumo esto a cadena en variable'
print(variable)
# Para elegir un caracter por medio de su posicion en la cadena 
print(variable[5])   
#Para elegir un caracter por medio de su posicion en la cadena 
print(variable[-1])  
#Para seleccionar caracteres por medio de su posicion en la cadena. Iniciando desde 0 y los espacios en blanco cuentan igualmente
print(variable[2:6])
#Para la cantidad de caracteres en la cadena de texto
print(len(variable))
#Devuelve el texto en mayusculas completo
print('Hola'.upper())
#Devuelve el texto en minisculas completo
print(variable.lower())
#Devuelve la primera letra en mayuscula
print(variable.capitalize())
#Eliminar los espacios en blancos en una cadena
cadena = '       Esto es una cadena con      muchos espacios      '
print(cadena)
print(cadena.strip())
#Reemplazar un valor especifico dentro de la cadena
cadena = 'Hola esto es un texto sin reemplazar'
print(cadena)
print(cadena.replace('sin reemplazar','reemplazado'))
#Operadores basicos matematicos
print(1+6)
print(8-5)
print(2*5)
print(8/2)
print(5**3)
print(5/2)
print(5%2)
print(-3)
#Operadores Booleanos | <> | = | == | <= | >= | != 
print(1 < 3)
print(1 > 5)
print(1 >= 9)
print(1 <= 0)
print(1 != 3)
print(5 == 6)
print(5 == 5)
print(6 == 4)  
#Operadores logicos |and | or | not
print(1 > 3 and 1 < 5) 
print(2 == 3 or 5 < 9)
print(1>2)
#Cadenas
print('Hola' + 'Jose')
print('Hola'  *   4)
print('Hola' + str(5))
print(int('34343'))
print(type('34343'))
print(type(int('34343')))
print(float(232))
print(bool(''))
print(bool(0))
print(bool(232))
print(bool('False'))