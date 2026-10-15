"""Exact corroboration of Phase 4 certificates; proofs are in the research note."""
from itertools import combinations
from math import ceil, comb


def advance(row, n, f):
    return [sum(f.get(y-z, 0)*a for z, a in enumerate(row))
            for y in range(n+1)]


def uniform(row, q):
    return all(row[i] == row[i+q] for i in range(len(row)-q))


def verify():
    origin_cases = 0
    ds = list(range(-3, 5))
    for bits in range(1, 1 << len(ds)):
        f = {d: 1 for i, d in enumerate(ds) if bits & (1 << i)}
        m, M = min(f), max(f)
        for q in range(1, 9):
            b = max(q-1, max(0, M)+max(0, 1-m)+q-2)
            h = b + ceil(q/max(M, 1-m))
            row = [1]
            rows = [row]
            for n in range(1, h+1):
                row = advance(row, n, f)
                rows.append(row)
            assert not any(rows[b]) or not all(uniform(r, q) for r in rows[b:])
            origin_cases += 1
    restarted_cases = 0
    for q in range(1, 13):
        for v in range(1, 13):
            b = q*(2*q+v+2)
            row = [int(y % q == b % q) for y in range(b+1)]
            f = {1-v: 1}
            T = ceil(q/v)
            assert uniform(row, q)
            for t in range(1, T+1):
                row = advance(row, b+t, f)
                assert uniform(row, q) == (t < T)
                assert any(row)
            restarted_cases += 1
    varying_cases = 0
    for q in range(1, 13):
        b = 4*q
        row = [int(y % q == 0) for y in range(b+1)]
        steps = [1]*(q-1) + [0]*(q-1)
        for t, d in enumerate(steps, 1):
            row = advance(row, b+t, {d: 1})
            assert uniform(row, q) and any(row)
        assert not uniform(advance(row, b+len(steps)+1, {0: 1}), q)
        varying_cases += 1
    binomial_cases = 0
    for q in range(1, 13):
        assert uniform([comb(q, y) for y in range(q+1)], q)
        for a, bb in [(1,1), (1,2), (2,1), (0,1), (1,0)]:
            for n in range(q+1, q+8):
                row = [comb(n,y)*a**(n-y)*bb**y for y in range(n+1)]
                assert not uniform(row, q)
                binomial_cases += 1
    print(f'Phase 4 obstruction: {origin_cases} binary origin cases; '
          f'{restarted_cases} sharp restarted homogeneous cases; '
          f'{varying_cases} sharp varying-kernel cases; '
          f'{binomial_cases} binomial exclusion cases.')


if __name__ == '__main__':
    verify()
