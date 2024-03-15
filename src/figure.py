"""
Geometric Figures abstract class
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """
    It counts some geometric characteristics
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        """
        It counts an area of figure given
        """

    @abstractmethod
    def get_perimeter(self):
        """
        It counts the perimeter
        """

    def add_area(self, figure2):
        """
        :return sum of two figures area
        :type figure2: object Figure
        """
        if not isinstance(figure2, Figure):
            raise ValueError('need Figure class argument')
        ss = self.get_area() + figure2.get_area()
        return ss
