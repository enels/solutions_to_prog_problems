from abc import ABCMeta, abstractmethod


class Polygon:
    """
    A base polygon class to construct other types of polygons
    """

    @abstractmethod
    def area(self):
        """
        :return: the area of the polygon type
        """

    @abstractmethod
    def perimeter(self):
        """
        :return: the perimeter of the polygon type
        """

