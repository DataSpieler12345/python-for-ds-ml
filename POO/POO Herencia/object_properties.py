class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class AncientMouse(Mouse):
    def __str__(self):
        return "My name is " + self.name

mus = AncientMouse("Caesar") # print "My name is Caesar"
print(mus)