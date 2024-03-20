# Using with open method to read the Example2.txt file

with open("Hallo.txt", "r") as f1:
    file_stuff = f1.read()
    
    print(file_stuff) # devuelve las lineas contenidas en el archivo txt. 
    print(file_stuff.rstrip()) # elimina espacios en blanco entre las lineas del txt file
    file_stuff = f1.readline()
    print(file_stuff)
    file_stuff = f1.readlines(1) # devuelve el/los caracteres de la linea. 
    print(file_stuff)
    file_stuff = f1.readlines(2)
    print(file_stuff)
    file_stuff = f1.readlines(3)
    print(file_stuff)
    file_stuff = f1.readlines(4)
    print(file_stuff)
    file_stuff = f1.readlines(5)
    print(file_stuff)

# using a loop to print out each line individually as follows

with open("Hallo.txt", "r") as f2:
    for line in f2:
        print(line)