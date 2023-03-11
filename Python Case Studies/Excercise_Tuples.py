# tuples con ()
tuple_1 = (1, 2, 4, 8)
# tuples sin () / Note = DataType are different
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)


# Example 2

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)


# Example 3 : What else can tuples do?

# the len() function accepts tuples, and returns the number of elements contained inside;
# the + operator can join tuples (we've shown this before)
# the * operator can multiply tuples, as well as lists;
# the in and not in operators work in the same way as for lists.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)

# One of the most useful properties of tuples is that they can appear on the left side of the assignment operator. This phenomenon has been seen before, when it was necessary to find a way to exchange the values between two variables.
print(-10 not in my_tuple)
