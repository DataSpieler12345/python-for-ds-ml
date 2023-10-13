#exercise 3
#get the radius and length of a circle in python 

# import math module 
import math
r = float(input(" enter the radius:  "))
area = math.pi*r**2
length = 2*math.pi*r 

print(f"the area is: {area:.2f}") #2 number of decimal
print(f"the length is: {length:.2f}") #2 number of decimal

print(f"the area is: {area}")
print(f"the length is: {length}") 