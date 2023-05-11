class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # Calls the superclass constructor to initialize the stack..
        Stack.__init__(self)
        # Initializes the counter to zero.
        self.__counter = 0

    def get_counter(self):
        # Returns the current value of the counter.
        return self.__counter

    def pop(self):
        # Pops a call to the pop method of the superclass and updates the counter.
        val = Stack.pop(self)
        self.__counter += 1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())  # output: 100