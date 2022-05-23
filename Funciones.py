#Funciones para reutilizar un codigo, mas legible
def esPar(numero):
   if numero%2 == 0:
      print("El numero es paar")
   else:
      print("El numero es impar")
      
numero = int(input("Dime un numero y te indicare si es paar o no "))
esPar(numero)
esPar(23)
esPar(21)
esPar(31)

#Funciones para reutilizar un codigo, mas legible
def esPar(numero):
   if numero%2 == 0:
      #print("El numero es paar")
      return True
   else:
      #print("El numero es impar")
      return False
      
numero = int(input("Dime un numero y te indicare si es paar o no "))
resultado = esPar(numero)
if resultado == True:
   print(f"El numero {numero} es paar")
else:
   print(f"El numero es {numero} es impar")
   