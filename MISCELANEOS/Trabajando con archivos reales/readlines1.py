from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('file.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in the file:", character_counter)
    print("Lines in the file:     ", line_counter)
except IOError as e:
    print("An I/O error occurred:", strerror(e.errno))
    