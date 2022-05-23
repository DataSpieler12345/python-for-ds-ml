#Creamos una variable de texto para el ejemplo que vamos a realiza
texto = "Esto es un texto para el ejemplo que vamos a realizar"

#empieza y termina con ver frase arriba. devuelve un booleano verdadero o falso 
print("La cadena empieza con: ", texto.startswith("Esto"))
print("La cadena termina con: ", texto.lower().endswith("Realizar".lower()))

#alinear texto
#centrado
print(texto.center(80, '+'))
print(texto.center(80, '/'))
print(texto.center(80, '*'))
print(texto.center(80, '-'))
print(texto.center(80, '_'))
print(texto.center(80, '|'))
longitudcadena = len(texto)
print(longitudcadena)
print(texto.center(longitudcadena+7, '-'))

#Añadiendo caracteres por la izquierda / alineado a la izquierda
print(texto.ljust(80, '-'))

#Alienando a la derecha 
print(texto.rjust(80, '0'))

#Eliminando partes de la cadena 
texto = "      Esto es una cadena co nespacios en blanco y algunos caracteres raros *-/6535-*-\/\/j   "
print(texto)
#print cadena sin espacios
print("Cadena sin espacios en blanco: ")
print(texto.strip())

#Sustituyendo caracteres en la cadena 
print(texto.replace("-","hola"))
print(texto)

