"""
inherited from Figure Class, it has the same methods
"""
from figure import Figure


class Rectangle(Figure):
    """
    Rectangle Figure class
    """

    def __init__(self, side_a, side_b):
        """
        :param args: triangle sides
        """
        super().__init__(name='Rectangle')

        self.side_a = side_a
        self.side_b = side_b

        self.__verify_rectangle()

    def __verify_rectangle(self):
        """
        :return: true if the rectangle given is a real one, raise error in other case
        """
        for v in (self.side_a, self.side_b):
            if not isinstance(v, (int, float)):
                raise ValueError('rectangle sides must be numbers')
            if v <= 0:
                raise ValueError('sides length must be greater than zero')

    def get_area(self):
        """
        :return: calculates rectangle area
        """
        s = self.side_b * self.side_a
        return s

    def get_perimeter(self):
        """
        :return: rectangle perimeter
        """
        p = 2 * (self.side_b + self.side_a)
        return p
