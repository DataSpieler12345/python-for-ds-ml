class A:
    def __init__(self,v = 1):
        self.v = v
 
    def set(self,v):
        self.v = v
        return v
 
 
a = A()
print(a.set(a.v + 1))