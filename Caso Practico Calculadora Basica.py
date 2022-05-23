#Ejercicio Practico / Calculadora basica 

def menu():
   print("1. Sumar")
   print("2. Restar")
   print("3. Multiplicar")
   print("4. Dividir")
   print("0. Salir")
   opcion = int(input("Que operacion deseas hacer?"))
   return opcion

def solicitarDatos():
   num1 = int(input("Introduce tu primer digito "))
   num2 = int(input("Introduce tu segundo digito segundo digito  "))
   if num2 == 0:
      print("El numero no puede ser 0\n")
      num2 = int(input("Introduce otra vez el segundo numero "))
   return num1, num2
   

def operacion(operador, num1, num2):
   if operador == "suma":
      resultado = num1 + num2 
   elif operador == "resta":
      resultado = num1 - num2 
   elif operador == "multiplica":
      resultado = num1 * num2
   elif operador == "divide":
      resultado = num1 / num2
   return resultado

while True:
   opcion = menu()
   if opcion == 1:
      num1, num2 = solicitarDatos()
      print(f"El resultado de {num1} + {num2} es = ")
      print(operacion("suma", num1, num2))   
   elif opcion == 2:
      num1, num2 = solicitarDatos()
      print(f"El resultado de {num1} - {num2} es = ")
      print(operacion("resta", num1, num2)) 
   elif opcion == 3:
      num1, num2 = solicitarDatos()
      print(f"El resultado de {num1} * {num2} es = ")
      print(operacion("multiplica", num1, num2)) 
   elif opcion == 4:
      num1, num2 = solicitarDatos()
      print(f"El resultado de {num1} / {num2} es = ")
      print(operacion("divide", num1, num2)) 
   elif opcion == 0:
      break 
   else:
      print("Introduce una opcion valida")
   print("\n")
print("Salir")
   
      
         