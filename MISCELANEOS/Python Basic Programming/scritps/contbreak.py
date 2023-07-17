lst = []

while 'END' not in lst:
    item = input("Input a value: ")
    if item == "":
        break
    elif item == "SKIP":
        continue
    lst.append(item)

if lst[-1] == "END":
    lst = lst[:-1]

print("The final list is: "+str(lst))