class A:
    def __str__(self):
        return 'a'
 
 
class B(A):
    def __str__(self):
        return 'b'
 
 
class C(B):
    pass
 
 
o = C()
print(o)