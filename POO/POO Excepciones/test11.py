class A:
    def __str__(self):
        return 'a'
 
 
class B:
    def __str__(self):
        return 'b'
 
 
class C(A, B):
    pass
 
 
o = C()
print(o)
 