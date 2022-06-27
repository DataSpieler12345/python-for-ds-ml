import re 
inb = input()
pattern = r"(1|8|9) [0-9]+"
match = re.match(pattern, inb)
if len(inb) == 8:
   if match:
      print("Valid")
   else:
      print("Invalid")
else:
   print("Invalid")