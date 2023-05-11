#The self parameter is also used to invoke other methods from within the class.
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()


