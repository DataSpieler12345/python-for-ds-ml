class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
	def m_bottom(self):
		print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    