# Define a class named Stack
class Stack: 
    def __init__(self):  # Define the constructor (__init__) function + self parameter.
        print("¡Hi!")


stack_object = Stack()


# Now let's add just one property to the new object, a list for the stack. We will name it stack_list.
class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))