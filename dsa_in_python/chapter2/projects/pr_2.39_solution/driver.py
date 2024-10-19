from isoscelestriangle import IsoscelesTriangle
from equilateraltriangle import EquilateralTriangle
from rectangle import Rectangle
from square import Square
from pentagon import Pentagon
from octagon import Octagon
from hexagon import Hexagon

shape = IsoscelesTriangle(6, 7)
print(shape.area())
print(shape.perimeter())

shape = EquilateralTriangle(6, 7)
print(shape.area())
print(shape.perimeter())

shape = Rectangle(6, 7)
print(shape.area())
print(shape.perimeter())

shape = Square(7, 7)
print(shape.area())
print(shape.perimeter())

shape = Pentagon(12)
print(shape.area())
print(shape.perimeter())

shape = Octagon(10)
print(shape.area())
print(shape.perimeter())

shape = Hexagon(8)
print(shape.area())
print(shape.perimeter())