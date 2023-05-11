class A:
    def __init__(self):
        self.a = 1
 
 
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = 2
        
b = B()
print(b.a)  # Output: 1
print(b.b)  # Output: 2