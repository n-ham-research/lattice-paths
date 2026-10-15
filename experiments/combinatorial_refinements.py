"""Exact classical profile formulas and direct sylvester congruence checks."""
from math import factorial, comb
from itertools import product
from collections import Counter


def profile_count(profile):
    """Nonnegative excursions: r[a] copies of -a, sum(a*r[a]) copies +1."""
    if any(a < 0 or r < 0 for a, r in profile.items()):
        raise ValueError('nonnegative sizes and multiplicities required')
    u = sum(a*r for a, r in profile.items())
    n = u + sum(profile.values())
    denominator = factorial(u+1)
    for r in profile.values():
        denominator *= factorial(r)
    return factorial(n)//denominator


def vertical_multiple_count(m, n):
    if m < 1 or n < 0:
        raise ValueError('m positive, n nonnegative')
    if n == 0:
        return 1
    return sum(comb(n,j)*2**j*comb(m*n,n-1-j) for j in range(n))//n


def packed_literature_count(m, n):
    """Novelli--Thibon (182), x=2, degree n = word length mn."""
    return sum(comb(m*n+1,k)*comb((m+1)*n-k,n-k)*(-1)**k*2**(n-k)
               for k in range(n+1))//(m*n+1)


def sylvester_classes(m, n):
    """Direct relation graph, no pattern-avoidance or GF assumptions."""
    length = m*n
    words = []
    if not length:
        return 1
    for k in range(1,n+1):
        for w in product(range(1,k+1), repeat=length):
            c = Counter(w)
            if len(c)==k and all(v % m == 0 for v in c.values()):
                words.append(w)
    unseen = set(words)
    classes = 0
    while unseen:
        classes += 1
        todo = [unseen.pop()]
        while todo:
            w = todo.pop()
            for i in range(length-1):
                a,c = sorted(w[i:i+2])
                if a == c or not any(a <= b < c for b in w[i+2:]):
                    continue
                v = w[:i]+(w[i+1],w[i])+w[i+2:]
                if v in unseen:
                    unseen.remove(v)
                    todo.append(v)
    return classes
