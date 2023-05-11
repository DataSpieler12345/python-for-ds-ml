#If you want the method to accept parameters other than self, you should:

#Place them after self in the method definition.
#Pass them as arguments during invocation without specifying self.

class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

