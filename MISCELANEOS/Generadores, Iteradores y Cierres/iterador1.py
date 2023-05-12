#We have created a class capable of iterating through the first n values (where n is a constructor parameter) of the Fibonacci numbers.

#Fib1 = 1
#Fib2 = 1
#Fibi = Fibi-1 + Fibi-2

#In other words:

#The first two numbers in the Fibonacci series are 1.
#Any other Fibonacci number is the sum of the previous two (e.g., Fib3 = 2, Fib4 = 3, Fib5 = 5, and so on).

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
    