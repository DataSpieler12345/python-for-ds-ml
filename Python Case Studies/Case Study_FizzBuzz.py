n = int(input())

for n in range(1, n, 2):
   if n % 3 == 0 and n % 5 == 0:
      pront("SoloLearn")
   elif n % 3 == 0:
      print("Solo")
   elif n % 5 == 0:
      print("Learn")
   else:
      print(n)