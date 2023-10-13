# exercise 2 
#create a program that asks for three numbers and determines which is the largest in the series
n1 = int(input("Please, enter a number: "))
n2 = int(input("Please, enter a number: "))
n3 = int(input("Please, enter a number: "))


if n1 >= n2 and n1 >= n3:
   print(f"The largest number is {n1}")
elif n2 >= n1 and n2 >= n3:
   print(f"The largest number is {n2}")
elif n3 >= n1 and n3 >= n2:
   print(f"The largest number is {n3}")
   