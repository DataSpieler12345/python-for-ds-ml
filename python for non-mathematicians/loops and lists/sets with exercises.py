#sets

a = {1,2,3,4}
b = {2,3,5,6}
c = {3,4,6,7}

# comparison of sets
# a == b
print(a == b)
# a union b 
print(a|b)
# a union c 
print(a|c)
# b union c 
print(b|c)
# a intersection b
print(a&b)
# a intersection c
print(a&c)
# b intersection c
print(b&c)


# mathematical operations between sets
print(a-b)

# symmetrical difference
print(a^b)
print(b^c)
print(a^c)