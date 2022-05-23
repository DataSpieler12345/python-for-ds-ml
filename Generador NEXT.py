 #Generadores con funcion que detecte y muestre los numeros impares
def impares():
   for numero in range(1,50,2):
      yield numero 
          
generador = impares()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print("Terminando  nexct uno a uno y pasamos a blucle FOR")
#for numero in generador:
   #print(numero)
#print(generador)
  
   