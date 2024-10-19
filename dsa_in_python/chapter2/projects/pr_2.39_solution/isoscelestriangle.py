from triangle import Triangle
from math import sqrt


class IsoscelesTriangle(Triangle):
    """
    Calculate the area dnd perimeter of an isosceles triangle
    """

    def __init__(self, base, height):
        super().__init__(base, height)

    def perimeter(self):
        """
        Calculate the perimter of an isosceles triangle
        :return: sume of all sides
        """

        # calculate the slant height
        slant_height = self._get_slant_height()

        return slant_height * 2 + self._base

    def _get_slant_height(self):
        """
        Calculate the slant height of the triangle
        :return: the slant height in int or float
        """

        return sqrt((self._base / 2)**2 + self._height**2)