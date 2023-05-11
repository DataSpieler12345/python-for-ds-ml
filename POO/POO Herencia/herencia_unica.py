class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB):
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())