"""
inherited from Figure Class, it has the same methods
"""
import math
from figure import Figure


class Circle(Figure):
    """
    Circle Figure class
    """

    def __init__(self, radius: float):
        """
        :param args: triangle sides
        """
        super().__init__(name='Circle')

        self.radius = radius

        self.__verify_circle()

    def __verify_circle(self):
        """
        :return: true if the radius is a positive number
        """
        if not isinstance(self.radius, (int, float)):
            raise ValueError('radius is not a number')

        if self.radius <= 0:
            raise ValueError('radius is less than zero')

    def get_area(self):
        """
        :return: calculates circle area
        """
        s = math.pi * self.radius ** 2
        return s

    def get_perimeter(self):
        """
        :return: triangle perimeter
        """
        p = 2 * math.pi * self.radius
        return p
