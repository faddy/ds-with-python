
class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Fraction(n, d)

    def __eq__(self, other):
        n1 = self.num * other.den
        n2 = other.num * self.den

        return n1 == n2
