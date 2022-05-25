from math import *
from enum import Enum

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    def __init__(self, x, y, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = x
            self.y = y
        elif system == CoordinateSystem.POLAR:
            self.x = x*cos(y)
            self.y = x*sin(y)
        # steps to add a new system
        # 1. augment CoordinateSystem
        # 2. change init method (hits the open close principle)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    # solution (create factory methods)

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho*cos(theta), rho*sin(theta))

    class Factory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho*cos(theta), rho*sin(theta))        


# p = Point(1, 2, CoordinateSystem.CARTESIAN)
# p2 = Point(1, 2, CoordinateSystem.POLAR)
# print(p, p2)

p = Point.new_cartesian_point(1,2)
p2 = Point.new_polar_point(1,2)
print(p)
print(p2)

p3 = Point.Factory.new_cartesian_point(3,4)