#variables 
a=30
b=40
c=50

# and 
r = ((a<b) and (b<c)) #true
print(r)

z = ((a>b) and (b<c)) #false
print(z)

# or 
k = ((a>b) or (b<c)) #true
print(k)

p = ((a<b) or (b<c)) #true
print(p)

# not  
i = not((a>b) or (b<c)) #false
print(i)

u = not((a<b) or (b<c)) #false
print(u)