#Importando del modulo random una funcion
from random import randint as azar 
continua = "s"
while(continua == "s" or continua == "S"):
   lanzaDado = azar(1,6)
   print("Has sacado un "+str(lanzaDado))
   continua = input("Continuamos(s/n)? ")
print("Ya no tiro mas el dado, hasta luego")