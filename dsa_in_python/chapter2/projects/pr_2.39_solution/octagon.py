from polygon import Polygon


class Octagon(Polygon):

    def __init__(self, sides_length):
        self._sides_length = sides_length
        self._n_sides = 8

    def area(self):
        """
        Get the area of the pentagon
        :return: area
        """

    def perimeter(self):
        """
        Get the perimeter of the pentagon
        :return: perimeter
        """

        return self._sides_length * self._n_sides
