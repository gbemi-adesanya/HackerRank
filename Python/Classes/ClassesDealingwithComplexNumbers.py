"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
"""

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)
        
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)
        
    def __mul__(self, no):
        # (a + b*i)(c + d*i) = ac + ad*i + bc*i - bd
        real = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real, imaginary)

    def __truediv__(self, no):
        """
        (a + b*i)         (a + b*i)       (c - d*i)         (ac - ad*i + bc*i + bd)             (ac + bd)         (bc - ad)
        ---------    =    ---------   .   ---------   =     -----------------------      =     -----------   +   ----------- * i
        (c + d*i)         (c + d*i)       (c - d*i)               (c^2 + d^2)                  (c^2 + d^2)       (c^2 + d^2)
        """
        conjugate_real = no.real
        conjugate_imaginary = -no.imaginary
        conjugate = Complex(*[conjugate_real, conjugate_imaginary])
        
        numerator = self.__mul__(conjugate)
        denominator = no.__mul__(conjugate).real
        
        real = numerator.real/denominator
        imaginary = numerator.imaginary/denominator
        return Complex(real, imaginary)

    def mod(self):
        real_sq = (self.real ** 2)
        imaginary_sq = (self.imaginary ** 2)
        
        real = math.sqrt(real_sq + imaginary_sq)
        imaginary = 0
        return Complex(real, imaginary)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
