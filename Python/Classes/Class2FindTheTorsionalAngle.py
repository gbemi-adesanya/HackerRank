"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
"""

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, no):
        # The subtraction function
        x_ = self.x - no.x
        y_ = self.y - no.y
        z_ = self.z - no.z
        return Points(x_, y_, z_)

    def dot(self, no):
        # Calculate the dot product
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        # Calculate the cross product
        yz = (self.y * no.z) - (no.y * self.z)
        xz = (self.z * no.x) - (no.z * self.x)
        xy = (self.x * no.y) - (no.x * self.y)
        return Points(yz, xz, xy)
        
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

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
