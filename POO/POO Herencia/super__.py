class Mouse:
    def __str__(self):
        return "Mouse"
 
 
class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()
 
 
doctor_mouse = LabMouse();
print(doctor_mouse) # print "Laboratory Mouse".