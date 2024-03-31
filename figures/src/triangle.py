"""
inherited from Figure Class, it has the same methods
"""
from math import sqrt
from figure import Figure


class Triangle(Figure):
    """
    Triangle Figure class
    """

    def __init__(self, line_a: float, line_b: float, line_c: float):
        """
        :param args: triangle sides
        """
        super().__init__(name='Triangle')

        self.line_a = line_a
        self.line_b = line_b
        self.line_c = line_c

        self.__verify_triangle()

    def __verify_triangle(self):
        """
        :return: true if the triangle given is a real one, raise error in other case
        """
        a = self.line_a
        b = self.line_b
        c = self.line_c

        for v in (a, b, c):
            if not isinstance(v, (int, float)):
                raise ValueError('parameters are not numbers')

        if not (a > 0 and b > 0 and c > 0):
            raise ValueError('parameters are less than zero')

        for el in (a, b, c):
            if el > a + b + c - el:
                raise ValueError('your triangle given is not a real one')

    def get_area(self):
        """
        :return: calculates triangle area using Heron formula
        """
        p = self.get_perimeter() / 2.0
        s = sqrt(p * (p - self.line_a) * (p - self.line_b) * (p - self.line_c))

        return s

    def get_perimeter(self):
        """
        :return: triangle perimeter
        """
        p = self.line_a + self.line_b + self.line_c
        return p
