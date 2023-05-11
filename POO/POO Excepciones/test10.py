class A:
    v = 2
 
 
class B(A):
    v = 1
 
 
class C(B):
    pass
 
 
o = C()
print(o.v)