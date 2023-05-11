#When you try to access an entity of any object, Python will try (in this order):

#Find it within the object itself.
#Find it in all classes involved in the object's inheritance line from the bottom up.
#If both attempts fail, an exception (AttributeError) will be generated.


#The first condition may need additional attention. As you know, all objects derived from a particular class may have different sets of attributes, and some of the attributes may be added to the object long after the object's creation.

#The example in the editor summarizes this in a three-level inheritance line.
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())