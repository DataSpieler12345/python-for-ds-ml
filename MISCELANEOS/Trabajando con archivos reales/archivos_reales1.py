from os import strerror

try:
    counter = 0
    stream = open('file.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in the file:", counter)
except IOError as e:
    print("An I/O error occurred: ", strerror(e.errno))

