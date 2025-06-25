import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        x1 = self.x - no.x 
        y1 = self.y - no.y
        z1 = self.z - no.z
        
        return Points(x1, y1, z1)
        
    def dot(self, no):
        
        x1 = self.x * no.x
        y1 = self.y * no.y
        z1 = self.z * no.z
        
        return x1 + y1 + z1
        
    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)

        
    def absolute(self):
        
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
