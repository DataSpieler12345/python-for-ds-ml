from os import strerror

try:
    file = open('newtext1.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("An I/O error occurred: ", strerror(e.errno))