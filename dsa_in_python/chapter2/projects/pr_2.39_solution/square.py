from quadrilateral import Quadrilateral


class Square(Quadrilateral):

    def __init__(self, width, height):
        if width == height:
            super().__init__(width, height)
        else:
            print("Sides must be equal for a square")
            exit()
