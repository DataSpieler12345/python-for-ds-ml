from pathlib import Path

file_path = Path('./files/users.txt') 

# if file_path.exists():

try:
   with open(file_path) as file:
      content = file.read()
   
      print(content)
except:
   print("sorry, it was not possible to read the file.")
   
   