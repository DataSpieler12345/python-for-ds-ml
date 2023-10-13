# exercise 1
#Create a program that asks for 2 numbers and obtains as a result which of them is even or if both of them are even.

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a second number: "))

if n1%2==0 and n2%2==0:
   print("both are even numbers")
elif n1%2==0 and n2%2!=0:
   print(f"{n1} its a even number")
elif n1%2!=0 and n2%2==0:
   print(f"{n2} its a even number")
else:
   print("both are odd numbers")