#Funcion SUM
def suma(num1, num2):
   resultado = num1 + num2 
   return resultado

num1 = int(input("Introduce el primer numero "))
num2 = int(input("Introduce el segundo numero "))

#Guardar el valor 
resultado = suma(num1, num2)


#Opcion extra para presentar data
print(f"La suma es igual {resultado}")