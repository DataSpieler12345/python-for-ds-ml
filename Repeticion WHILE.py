#WHILE Repeticion o Bucle

#Tabla de multiplicar
tabla = int(input("Que tabla quieres calcular? "))
#Creamos una variable contador
contador = 1
print(f"Tabla del {tabla}")
#Repetion de multiplicacion
while (contador<11):
   resultado = tabla * contador
    #Mostramos la tabla
   print(f"{tabla} por  {contador} es igual a {resultado}\n")
   #Comprobamos si vale 4 y salimos 
   if contador == 4:
      print(f"El contador es igual a 4 y no continua")
      break
   #Incremento del contador
   contador = contador + 1
print("Fin de la tabla....")
