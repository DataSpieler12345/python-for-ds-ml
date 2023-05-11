class Mouse:
    pass
 
 
class LabMouse(Mouse):
    pass
 
 
mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse)) # print"True False".