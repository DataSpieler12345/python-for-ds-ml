from pathlib import Path

# read files
# file = open('./files/users.txt') #relative route
file_path = Path('./files/users.txt') 
file = open(file_path) #Posix

content = file.read()
file.close()

print(content)

