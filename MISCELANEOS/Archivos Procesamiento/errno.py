import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("File does not exist.")
    elif exc.errno == errno.EMFILE:
        print("Too many open files.")
    else:
        print("The error number is:", exc.errno)