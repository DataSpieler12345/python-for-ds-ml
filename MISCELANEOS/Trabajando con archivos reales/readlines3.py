from os import strerror

try:
    ccnt = lcnt = 0
    s = open('file.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in the file:", ccnt)
    print("Lines on file:     ", lcnt)
except IOError as e:
    print("An I/O error occurred:", strerror(e.errno))