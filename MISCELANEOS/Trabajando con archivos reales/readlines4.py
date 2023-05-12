from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('file.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in the file:", ccnt)
	print("Lines in the file:     ", lcnt)
except IOError as e:
	print("An I/O error occurred: ", strerror(e.errno))