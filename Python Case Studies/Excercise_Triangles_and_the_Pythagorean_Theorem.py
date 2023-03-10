# Triangles and the Pythagorean Theorem

# Look at the code in the editor. It asks the user for three values. Then it makes use of the is_a_triangle function. The code is ready to run.

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the length of the first side: '))
b = float(input('Enter the length of the second side: '))
c = float(input('Enter the length of the third side: '))

if is_a_triangle(a, b, c):
    print('Yes, if it can be a triangle.')
else:
    print('No, it cannot be a triangle.')
