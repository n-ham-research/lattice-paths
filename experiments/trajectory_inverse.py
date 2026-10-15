"""Exact endpoint inversion and finite-support trajectory checks.

All paths start at (0,0), have steps (1,d), and satisfy 0<=y<=n
at each integer layer. The empty path has weight one.
"""
from fractions import Fraction
from itertools import product


def endpoint_rows(weights, horizon):
    rows = [[Fraction(1)]]
    for n in range(1, horizon + 1):
        rows.append([sum((rows[-1][z] * weights.get(y-z, 0)
                          for z in range(n)), Fraction(0))
                     for y in range(n+1)])
    return rows


def recover_weights(rows):
    """Recover W_N from complete rows; reject zero edge pivots/inconsistent data."""
    if not rows or rows[0] != [1]:
        raise ValueError('The empty path row must be [1]')
    if len(rows) == 1:
        return {}
    if any(len(row) != n+1 for n,row in enumerate(rows)):
        raise ValueError('Wrong row length')
    f = {0: Fraction(rows[1][0]), 1: Fraction(rows[1][1])}
    for n in range(2, len(rows)):
        prev = rows[n-1]
        if len(prev) != n or len(rows[n]) != n+1:
            raise ValueError('Wrong row length')
        if not prev[0] or not prev[-1]:
            raise ValueError('Zero boundary pivot')
        f[n] = (rows[n][n] - sum(prev[z]*f[n-z] for z in range(1,n))) / prev[0]
        f[1-n] = (rows[n][0] - sum(prev[z]*f[-z] for z in range(n-1))) / prev[-1]
    if endpoint_rows(f, len(rows)-1) != rows:
        raise ValueError('Inconsistent endpoint data')
    return f


def residue_uniform(row, q):
    return all(row[y] == row[y+q] for y in range(len(row)-q))


def obstruction_window(support, q, first=0):
    """Rows B..H uniform imply row B=0 for nonnegative finite support."""
    if not support or q < 1:
        raise ValueError('Nonempty support and positive modulus required')
    left = max(0, max(support))
    right = max(0, 1-min(support))
    b = max(first, q-1, left+right+q-2)
    ceiling = (b+q)//q
    return b, q*(ceiling+1)-1


def verify():
    # Exhaustive binary inverse recovery on W_5, with 0 and 1 present.
    n = 5
    free = [d for d in range(1-n,n+1) if d not in (0,1)]
    inverse_cases = 0
    for bits in product((0,1), repeat=len(free)):
        f = dict(zip(free,bits)) | {0:1,1:1}
        assert recover_weights(endpoint_rows(f,n)) == f
        inverse_cases += 1
    # Finite-support obstruction: every subset of [-2,3], moduli 1..4.
    obstruction_cases = 0
    for bits in product((0,1), repeat=6):
        f = {d:1 for d,bit in zip(range(-2,4),bits) if bit}
        if not f:
            continue
        for q in range(1,5):
            b,h = obstruction_window(f,q)
            rows = endpoint_rows(f,h)
            if all(residue_uniform(rows[n],q) for n in range(b,h+1)):
                assert not any(rows[b])
            obstruction_cases += 1
    # Signed rational inversion uses no positivity.
    weighted = {d: Fraction(1 if d % 2 == 0 else -1,abs(d)+1) for d in range(-4,6)}
    assert recover_weights(endpoint_rows(weighted,5)) == weighted
    # Infinite nonidentifiability without reachability: arbitrary negative jumps invisible.
    assert endpoint_rows({0:1},8) == endpoint_rows({d:1 for d in range(-8,1)},8)
    exceptional = {d:1 for d in (-5,-3,0,1,4,6)}
    assert all(residue_uniform(row,5) for row in endpoint_rows(exceptional,6))
    assert exceptional.get(-4,0) != exceptional[1]
    return {'binary_inverse_cases':inverse_cases,
            'finite_support_obstruction_cases':obstruction_cases,
            'signed_rational_inverse_cases':1,
            'nonidentifiability_comparisons':1,
            'nonperiodic_uniform_prefix_counterexamples':1}


if __name__ == '__main__':
    print(verify())
