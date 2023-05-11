#There is a fundamental requirement: a method is obliged to have at least one parameter (there are no methods without parameters; a method can be invoked without an argument, but it cannot be declared without parameters).

#The first (or only) parameter is usually named self. We suggest you keep naming it this way; giving it other names may cause unexpected surprises.

#The name self suggests the purpose of the parameter: it identifies the object for which the method is invoked.

#If you are going to invoke a method, you should not pass the argument for the self parameter, Python will set it up for you.

class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()