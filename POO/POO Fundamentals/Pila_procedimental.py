#create a empty list 
stack = []

# create the function to push the value inside of the list 

def push(val):
   stack.append(val)

# then use the function pop 

def pop():
   val = stack[-1]
   del stack[-1]
   return val

#test your own push function
push(3)
push(2)
push(1)

#print the function pop
print(pop())
print(pop())
print(pop())
