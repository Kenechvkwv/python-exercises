# Exercise 3.1

"""
The archive contains geometry module (i.e. geom.py) that contains two classes,Coordinate and Reactangle.The Coordinate class models a geometric point by representing the x and y coordinates of the point. The rectangle class models a rectangle by accepting the top left point and bottom right point of a rectangle. In your test function you need to create instances of two points by using the coordinate class and then create an instances of two points by using the coordinate class and then create an instance of a rectangle by using the two points. Your test function should then call different methods of the rectangle and points to test those
"""

# geometry module: geom.py


import math  # Import math module for sqrt function


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another):
        xdist = abs(self.x - another.x)
        ydist = abs(self.y - another.y)
        return math.sqrt(xdist**2 + ydist**2)


def test_coord_dist_method():
    print("Testing distance method for Coordinate class")
    point1 = Coordinate(2, 2)
    point2 = Coordinate(3, 4)
    distance = point1.distance(point2)
    print("Distance between points:", distance)


class Rectangle:
    def __init__(self, tl, br):
        self.tl = tl
        self.br = br
        self.width = abs(tl.x - br.x)
        self.height = abs(tl.y - br.y)

    def area(self):
        return self.width * self.height


def test_rect_surface_method():
    print("\nTesting area method for Rectangle class")
    top_left = Coordinate(1, 5)
    bottom_right = Coordinate(4, 2)
    rect = Rectangle(top_left, bottom_right)
    area = rect.area()
    print("Area of the rectangle:", area)


def main():
    test_coord_dist_method()
    test_rect_surface_method()


main()
