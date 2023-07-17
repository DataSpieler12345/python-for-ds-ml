lst = []

while 'END' not in lst:
    lst.append(input("Input a value: "))

lst = lst[:-1]
print("The final list is: "+str(lst))