class Classy:
    def visible(self):
        print("unhide")
 
    def __hidden(self):
        print("Hide")
 
 
obj = Classy()
obj.visible()
 
try:
    obj.__hidden()
except:
    print("fail")
 
obj._Classy__hidden()