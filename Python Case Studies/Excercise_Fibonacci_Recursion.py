# There is something else that we want to show: it is recursion.

# This term can describe many different concepts, but one of them refers to computer programming.

# Here, recursion is a technique where a function invokes itself.

# Both the factorial and the Fibonacci series are the best options to illustrate this phenomenon.

# The Fibonacci series is a clear example of recursion. We already told you that:

# Fibi = Fibi-1 + Fibi-2.

# The number i refers to the number i-1, and so on until you get to the first two.

# Can it be used in the code? Of course it can. It can make the code shorter and clearer.

# The second version of the fib() function makes direct use of recursion:

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
for n in range(1, 10):
    print(n, "->", fib(n))