class Snake:
    def __init__(self):
        self.victims = 0
    
    def increment(self):
        self.victims += 1


#Redefines the constructor of the Snake class to have a parameter that initializes the victims field with a value passed to the object during construction.

class Snake:
    def __init__(self, initial_victims=0):
        self.victims = initial_victims
    
    def increment(self):
        self.victims += 1