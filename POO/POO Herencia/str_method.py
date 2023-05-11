class Mouse:
    def __init__(self, name):
        self.my_name = name
 
 
    def __str__(self):
        return self.my_name
 
 
the_mouse = Mouse('mickey')
print(the_mouse) # print "mickey".