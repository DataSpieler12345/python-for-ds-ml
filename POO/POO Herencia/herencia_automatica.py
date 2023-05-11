class Mouse:
    Population = 0

    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hello, my name is " + self.name

class LabMouse(Mouse):
    def __init__(self, name, experiment):
        # call the constructor of the superclass to initialize the mouse name
        super().__init__(name)
        self.experiment = experiment

# create a LabMouse instance
professor_mouse = LabMouse("Prof Mouse", "memory experiment")
# print instance and current mouse population
print(professor_mouse, Mouse.Population) # should print "Hello, my name is Prof Mouse 1"