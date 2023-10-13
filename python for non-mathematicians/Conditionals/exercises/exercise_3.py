# exercise 3
#Create a program that compares two names, and check if there is a match or not, if both names start with the same letter or if they end with the same letter.

name1 = input("Enter a name 1: ")
name2 = input("Enter a name 2: ")

if name1[0] == name2[0] or name1[-1] == name2[-1]:
   print("matches found")
else:
   print("matches not found")
   