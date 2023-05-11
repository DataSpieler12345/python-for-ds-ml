class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " und lebe ich in " + Sample.__module__)
 
 
obj = Sample()
obj.myself()