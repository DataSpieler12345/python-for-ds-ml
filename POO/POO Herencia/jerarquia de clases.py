class One:
    def do_it(self):
        print("do_it de One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it de Two")


one = One()
two = Two()

one.doanything()
two.doanything()