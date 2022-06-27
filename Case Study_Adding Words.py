def concatenate(*args):
   result = None
   for i in args:
      if result == None:
         result = 1 
      else:
         result += "-" + i
         
   return result 

print(concatenate("I", "Love", "Python", "!"))
