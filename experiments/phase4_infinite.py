#!/usr/bin/env python3
"""Exact checks for modulus-two actual-trajectory rigidity (not a proof)."""
from fractions import Fraction as F
from itertools import product


class Quadratic:
    """Exact a+b*sqrt(2), only for the explicit sharpness example."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Quadratic) else Quadratic(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Quadratic(self.a+other.a, self.b+other.b)
    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        return Quadratic(self.a*other.a+2*self.b*other.b,
                         self.a*other.b+self.b*other.a)
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        d = other.a*other.a-2*other.b*other.b
        return self*Quadratic(other.a/d, -other.b/d)

    def __eq__(self, other):
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f'({self.a})+({self.b})sqrt(2)'


def rows(weights, horizon):
    result = [[F(1)]]
    for n in range(1, horizon+1):
        prev = result[-1]
        result.append([sum(prev[z]*weights.get(y-z, 0) for z in range(n))
                       for y in range(n+1)])
    return result


def uniform(row, q=2):
    return all(row[y] == row[y+q] for y in range(len(row)-q))


def rational_prefix(x):
    c = (x*x-x+2)/(x+1)
    a = (3*x-1)/(x+1)
    return {0: 1, 1: 1, -1: x, 2: x, -2: c, 3: c, -3: a, 4: a}


def verify():
    survivors = []
    for bits in product((0, 1), repeat=4):
        f = dict(zip((-2, -1, 2, 3), bits)) | {0: 1, 1: 1}
        if all(uniform(row) for row in rows(f, 3)):
            survivors.append(f)
    assert len(survivors) == 1 and all(survivors[0].values())
    q3_survivors = []
    for bits in product((0, 1), repeat=6):
        f = dict(zip((-3, -2, -1, 2, 3, 4), bits)) | {0: 1, 1: 1}
        if all(uniform(row, 3) for row in rows(f, 4)):
            q3_survivors.append(f)
    assert len(q3_survivors) == 2
    assert all(all(f[d] == f[d+3] for d in f if d+3 in f)
               for f in q3_survivors)
    assert all(uniform(row, 3) for row in rows({0: 1, 1: 1}, 3))
    checked = 0
    for denominator in range(1, 21):
        for numerator in range(denominator, 4*denominator+1):
            x = F(numerator, 2*denominator)
            f = rational_prefix(x) | {-4: 1, 5: 1}
            p = rows(f, 5)
            assert all(uniform(row) for row in p[:5])
            c0 = x*x+2*x+3
            obstruction = -2*c0*(x-1)**2*(x*x+2*x-1)/(x+1)**2
            assert p[5][1]-p[5][3] == obstruction
            assert (obstruction == 0) == (x == 1)
            checked += 1
    # Optimal rational horizon: nonnegative nonconstant weights pass through 4.
    example = rational_prefix(F(1, 2))
    assert all(v >= 0 for v in example.values())
    assert all(uniform(row) for row in rows(example, 4))
    assert not uniform(rows(example, 5)[5])
    # Independent explicit weighted words for this exact rational example.
    words = [(0, F(1))]
    for n in range(1, 6):
        words = [(height+d, weight*w) for height, weight in words
                 for d, w in example.items() if 0 <= height+d <= n]
        explicit = [sum(w for height, w in words if height == y) for y in range(n+1)]
        assert explicit == rows(example, n)[-1]
    # Optimal real horizon: the only additional algebraic branch passes 5,
    # but the necessary next weight is 7-5sqrt(2)<0.
    s = Quadratic(0, 1)
    f = {0: Quadratic(1), 1: Quadratic(1), -1: s-1, 2: s-1,
         -2: 3*s-3, 3: 3*s-3, -3: 3-2*s, 4: 3-2*s,
         -4: 6*s-7, 5: 6*s-7}
    assert all(uniform(row) for row in rows(f, 5))
    prev = rows(f, 5)[-1]
    bottom_known = sum(prev[z]*f[-z] for z in range(5))
    target2 = sum(prev[z]*f[2-z] for z in range(6))
    assert (target2-bottom_known)/prev[-1] == 7-5*s
    # Boundary value transcriptions used in the note's algebra table.
    for n, row in enumerate(rows(f, 5)):
        assert all(v == row[y % 2] for y, v in enumerate(row))
    print(f'phase4 infinite: 16 modulus-two / 64 modulus-three binary assignments; {checked} rational parameter checks; explicit weighted words through 5; exact irrational branch passed')


if __name__ == '__main__':
    verify()
