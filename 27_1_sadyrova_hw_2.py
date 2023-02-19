class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_perimeter(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        self.__side_length = value

    def calculate_perimeter(self):
        return self.__side_length*4

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        return (f' Square side length: {self.__side_length}{self.unit}, perimeter: {self.calculate_perimeter()}{self.unit}, area: {self.calculate_area()}{self.unit}')


square = Square(4)
print(square.info())
print(square. calculate_perimeter())
print(square. calculate_area())


class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


    def calculate_perimeter(self):
        return self.__length*2+self.__width*2

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        return (f' Rectangle  length: {self.__length}{self.unit} width: {self.__width}{self.unit}, perimeter: {self.calculate_perimeter()}{self.unit}, area: {self.calculate_area()}{self.unit}')

rectangle = Rectangle(4, 3)
print(rectangle.info())
print(rectangle. calculate_perimeter())
print(rectangle. calculate_area())

