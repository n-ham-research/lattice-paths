"""Exact unrestricted composition models, with zero displacement excluded."""
from math import comb, factorial, prod


def sparse_down(n, y, q):
    """Steps (1,1-q*k), k>=0; n horizontal unit steps."""
    if n == 0:
        return int(y == 0)
    if n < 0 or q < 1 or (n-y) % q or y > n:
        return 0
    k = (n-y)//q
    return comb(n+k-1, k)


def residue_endpoint(n, q, wedge=False):
    """Every supported endpoint; heights are multiples of positive q."""
    if n < 0 or q < 1:
        raise ValueError('n>=0 and q>=1 required')
    return prod((2 if wedge else 1)*(j//q)+1 for j in range(n))


def arbitrary_positive_x(x, y, increments, vertical=False):
    """Steps (a,b), a>=1,b in increments; optional (0,1).

    A vector is one step; increments must be distinct. Finite endpoint count
    follows from k<=x and v=y-s<=y-k*min(increments).
    """
    increments = tuple(increments)
    if not increments or len(set(increments)) != len(increments):
        raise ValueError('nonempty distinct increments required')
    if x < 0:
        return 0
    if x == 0:
        return int(y >= 0) if vertical else int(y == 0)
    answer = 0
    distribution = {0: 1}
    for k in range(1, x+1):
        next_distribution = {}
        for s,c in distribution.items():
            for b in increments:
                next_distribution[s+b] = next_distribution.get(s+b,0)+c
        distribution = next_distribution
        if vertical:
            ways = sum(c*comb(y-s+k,k) for s,c in distribution.items() if y>=s)
        else:
            ways = distribution.get(y,0)
        answer += comb(x-1,k-1)*ways
    return answer


def finite_progress(n, steps):
    """Full columns 0..n for a finite set with strictly positive x."""
    steps = set(steps)
    if any(a<=0 for a,b in steps):
        raise ValueError('positive horizontal increments required')
    columns = [{0:1}]+[{} for _ in range(n)]
    for x in range(n+1):
        for y,c in list(columns[x].items()):
            for a,b in steps:
                if x+a<=n:
                    dest=columns[x+a]
                    dest[y+b]=dest.get(y+b,0)+c
    return columns
