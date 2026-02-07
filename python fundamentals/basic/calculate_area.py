from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def calculate_area(self):
        return self.radius * self.radius

class Triangle(Shape):

    def __init__(self, side1, side2):
        self._side1 = side1
        self._side2 = side2

    @property
    def side1(self):
        return self._side1
    @property
    def side2(self):
        return self._side2

    def calculate_area(self):
        return (2 * self.side1) + (2 * self.side2)