for line in open("file.txt", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')