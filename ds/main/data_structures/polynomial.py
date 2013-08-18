
import random


class Polynomial(object):

    def __init__(self):
        self.poly = {}


    def __call__(self, x):
        return self.evaluate(x)


    def add_term(self, degree, coeff):
        '''
        - allow add(0, 0)  [this is polynomial 0]
        - overwrite if same degree
        '''
        if degree < 0:
            raise Exception()

        if coeff == 0 and degree != 0:
            return

        self.poly[degree] = float(coeff)


    def evaluate(self, x):
        if x is None: return None

        total = 0
        for degree, coeff in self.poly.iteritems():
            total += coeff * (x**degree)

        return total


    def differential(self):
        # calulate differential of each term, add to a new polynomial object
        if not self.poly:
            return None

        diff = Polynomial()

        for degree, coeff in self.poly.iteritems():
            new_coeff = degree * coeff
            new_degree = degree - 1 if degree != 0 else 0
            diff.poly[new_degree] = new_coeff

        return diff


    def __repr__(self):
        s = []
        for degree in sorted(self.poly.keys(), reverse=True):
            if degree == 0 and self.poly[degree] == 0:
                continue

            coeff = '({0})'.format(self.poly[degree])
            term = '{0}x^{1}'.format(coeff, degree) if degree else coeff
            s.append(term)

        return ' + '.join(s)
            


def cube_root(n):

    threshold = .00005
    f = Polynomial()
    f.add_term(3, 1)
    f.add_term(0, -27)

    x0 = random.randint(0, n)

    while f(x0) > threshold:
        df = f.differential()
        x0 = x0 - (f(x0) /  df(x0))

    return x0
