class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass
    def info(self):
        pass

import math
class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value


    def calculate_area(self):
        return   math.pi * self.__radius**2

    def info(self):
        return (f' Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}')


circle = Circle(2)
print(circle.info())
print(circle.calculate_area())


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        self.__side_b = value



    def calculate_area(self):
        return (self.__side_a * self.__side_b)/2

    def info(self):
        return (f' RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area()}{self.unit}')

rightTriangle = RightTriangle(4, 3)
print(rightTriangle.info())
print(rightTriangle. calculate_area())
