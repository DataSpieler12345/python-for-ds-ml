# While loop iteration
number = 0
while number < 20:
      print(f"Number of iterations: {number}")
      number += 1
      

# While loop iteration with square root
import math 
num = int(input("Please, enter a number: "))

while num < 0:
   print("Please, enter a positive number: ")
   num=int(input("Please, again enter a positive number: "))
print(f"The result of the square root is: {math.sqrt(num):.2f}")