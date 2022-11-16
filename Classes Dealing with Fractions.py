# Path: Classes Dealing with Fractions.py
from fractions import Fraction

class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __abs__(self):
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power):
        return Fraction(self.numerator ** power, self.denominator ** power)

    def __radd__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __rsub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __rmul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rtruediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __rpow__(self, power):
        return Fraction(self.numerator ** power, self.denominator ** power)

    # def __repr__(self):
    #     return str(self.numerator) + "/" + str(self.denominator)

    # def __str__(self):
    #     if self.denominator == 0:
    #         result = "%.2f+0.00i" % (self.numerator)
    #     elif self.numerator == 0:
    #         if self.denominator >= 0:
    #             result = "0.00+%.2fi" % (self.denominator)
    #         else:
    #             result = "0.00-%.2fi" % (abs(self.denominator))
    #     elif self.denominator > 0:
    #         result = "%.2f+%.2fi" % (self.numerator, self.denominator)
    #     else:
    #         result = "%.2f-%.2fi" % (self.numerator, abs(self.denominator))
    #     return result

if __name__ == '__main__':
    a = Fraction(*map(int, input().split()))
    b = Fraction(*map(int, input().split()))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a == b)
    print(a < b)
    print(a > b)
    print(a <= b)
    print(a >= b)
    print(a != b)
    print(abs(a))
    print(abs(b))
    print(pow(a, int(input())))
    print(pow(b, int(input())))
