from polygon import Polygon


class Quadrilateral(Polygon):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        """
        get the area of the quad
        :return: area
        """

        return self._width * self._height

    def perimeter(self):
        """
        get the perimeter of the quad
        :return: perimeter
        """

        return self._width * 2 + self._height * 2