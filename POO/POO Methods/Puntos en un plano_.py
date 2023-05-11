import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # initialize properties as private
        self._x = x
        self._y = y

    def getx(self):
        # return the x-coordinate of the point
        return self._x

    def gety(self):
        # return the y-coordinate of the point
        return self._y

    def distance_from_xy(self, x, y):
        # calculate the distance between the point stored inside the object and the other point given by the coordinates (x, y)
        dx = self._x - x
        dy = self._y - y
        return math.hypot(dx, dy)

    def distance_from_point(self, point):
        # calculate the distance between the point stored inside the object and another given Point object
        dx = self._x - point.getx()
        dy = self._y - point.gety()
        return math.hypot(dx, dy)


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2)) # expected output: 1.4142135623730951
print(point2.distance_from_xy(2, 0)) # expected output: 1.4142135623730951