from polygon import Polygon


class Hexagon(Polygon):

    def __init__(self, sides_length):
        self._sides_length = sides_length
        self._n_sides = 6

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
