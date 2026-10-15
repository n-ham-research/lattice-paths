"""Direct finite enumeration of fixed convex polygon dissections.

Vertices have cyclic order 0,...,sides-1; the prescribed base is
(0,sides-1). Rotations/reflections are not identified. The base is not an
extra choice. This module does not generate trees or excursions.
"""
from collections import Counter
from itertools import combinations
from math import comb


def crossing(first, second):
    """Whether two ordered endpoint pairs cross in their interiors."""
    a, b = first
    c, d = second
    return a < c < b < d or c < a < d < b


def face_sizes(sides, diagonals):
    """Split polygon faces by an already noncrossing diagonal collection."""
    faces = [tuple(range(sides))]
    for a, b in diagonals:
        containing = [face for face in faces if a in face and b in face]
        if len(containing) != 1:
            raise ValueError('diagonals must be distinct and noncrossing')
        face = containing[0]
        faces.remove(face)
        i, j = sorted((face.index(a), face.index(b)))
        if j == i + 1 or (i == 0 and j == len(face)-1):
            raise ValueError('a diagonal must be internal to its current face')
        faces.extend((face[i:j+1], face[j:] + face[:i+1]))
    return tuple(len(face) for face in faces)


def enumerate_even_dissections(max_edges=10):
    """Return ordinary dissection counts and number of tested subsets.

    Summing even face sizes equals boundary sides plus twice the diagonal
    count, so only even-sided boundary polygons can contribute. Ordinary
    polygons with even faces have at least four sides. The formal one-edge
    object is deliberately excluded.
    """
    counts = Counter()
    tested = 0
    for sides in range(4, max_edges+1, 2):
        possible = [(a, b) for a in range(sides)
                    for b in range(a+2, sides) if (a, b) != (0, sides-1)]
        for number in range(min(max_edges-sides, len(possible))+1):
            for diagonals in combinations(possible, number):
                tested += 1
                if any(crossing(a, b) for a, b in combinations(diagonals, 2)):
                    continue
                if all(size % 2 == 0 for size in face_sizes(sides, diagonals)):
                    counts[sides+number] += 1
    return dict(sorted(counts.items())), tested


def parity_formula(edges):
    """A067955 coefficient with parity restriction and formal a(1)=1."""
    if not isinstance(edges, int) or edges < 1:
        raise ValueError('edges must be a positive integer')
    if edges == 1:
        return 1
    numerator = sum(comb(edges, j) * comb((edges-3-j)//2, j-1)
                    for j in range(1, (edges-1)//3+1)
                    if j % 2 == (edges-1) % 2)
    quotient, remainder = divmod(numerator, edges)
    if remainder:
        raise ArithmeticError('Lagrange coefficient is not integral')
    return quotient
