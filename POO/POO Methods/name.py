
#Can you predict the result of the following code?
class Snake:
    pass
 
 
class Python(Snake):
    pass
 
 
print(Python.__name__, 'es una', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be a', Python.__name__)

#Output 
#Python is a snake
#Snake can be a python