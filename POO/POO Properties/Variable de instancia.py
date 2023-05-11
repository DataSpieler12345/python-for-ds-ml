class ExampleClass:
    def __init__(self, val = 1):
        self.first = val #first instance of the class
 
    def set_second(self, val):
        self.second = val # the class has a second instance called second  
 
 
example_object_1 = ExampleClass() # has just 1 property called first
example_object_2 = ExampleClass(2) #has 2 properties called first and second
 
example_object_2.set_second(3) # has just 1 property called third
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
 
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)