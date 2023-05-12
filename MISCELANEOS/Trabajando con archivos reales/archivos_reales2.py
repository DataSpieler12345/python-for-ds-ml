from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCharacters in the file:", counter)
except IOError as e:
    print("An I/O error occurred: ", strerror(e.errno))