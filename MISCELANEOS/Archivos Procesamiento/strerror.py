from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Processing goes here.
    s.close()
except Exception as exc:
    print("File could not be opened:", strerror(exc.errno))
    