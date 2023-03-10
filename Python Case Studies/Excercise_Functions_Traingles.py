# Now we will work with triangles. We will start with a function that checks whether three sides of certain lengths can form a triangle.

# In school we learned that the arbitrary sum of two sides has to be greater than the length of the third side.

# This will not be difficult. The function will have three parameters - one for each side.

# It will return True if all sides can form a triangle, and False otherwise. In this case, is_a_triangle is a good name for such a function.

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))