"""
inherited from Rectangle Class, from Figure class
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Square Figure class
    """

    def __init__(self, side):
        """
        :param args: square sides
        """
        super().__init__(side, side)
