class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("down")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()