from polygon import Polygon


class Triangle(Polygon):


    def __init__(self, base, height):
        self._base = base
        self._height = height

    def area(self):
        """
        Calculate the area of the triangle
        :return: area in float or int
        """

        return 0.5 * self._base * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the triangle
        :return:
        """

        # assuming all sides are equal
        return self._base * 3