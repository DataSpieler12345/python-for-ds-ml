# tabla de multiplicar con FOR 
tabla = int(input("Cual tabla deseas calcular "))
print(f"Tabla del {tabla}")
#repetir mentras sea menor que 11
for contador in range(1,11):
   resultado = tabla * contador
   print(f"E{tabla} por {contador} es igual a {resultado}")
print("Fin de la tabla")

#ejemplo FOR con lista
nombres = ["Jose","M Mar", "Lucia","Eva"]
for nombre in nombres:
   print(f"Hola, {nombre}")
print("Fin de la lista")

#mostrar 100 numeros
for numero in range(100):
   print(numero)
   print(numero+1)