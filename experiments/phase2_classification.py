"""Independent exhaustive finite evidence for phase2-classification.md.

The proof is mathematical; this checks all binary jump indicators on the
observable window, including indicators with no reachable origin paths.
Run from the repository root: python3 experiments/phase2_classification.py
"""

from itertools import product


def direct_regular(source, target, allowed, q):
    for residue in range(q):
        source_cell = [z for z in source if z % q == residue]
        for target_residue in range(q):
            counts = {
                sum(y - z in allowed for z in source_cell)
                for y in target if y % q == target_residue
            }
            if len(counts) > 1:
                return False
    return True


def boundary_regular(source, target, allowed, q):
    target = set(target)
    for residue in range(q):
        cell = [z for z in source if z % q == residue]
        if cell:
            for y in target:
                if y + q in target:
                    if ((y - min(cell) + q in allowed)
                            != (y - max(cell) in allowed)):
                        return False
    return True


def main():
    triangular_cases = 0
    for nmax in range(1, 7):
        window = list(range(1 - nmax, nmax + 1))
        for bits in product((0, 1), repeat=len(window)):
            allowed = {d for d, bit in zip(window, bits) if bit}
            for q in range(1, 8):
                actual = all(direct_regular(range(n), range(n + 1), allowed, q)
                             for n in range(1, nmax + 1))
                expected = nmax < q or all(
                    (d in allowed) == (e in allowed)
                    for d in window for e in window if (d - e) % q == 0
                )
                assert actual == expected, (nmax, q, allowed)
                triangular_cases += 1

    interval_cases = 0
    intervals = [range(0)] + [range(a, b + 1)
                             for a in range(-2, 3) for b in range(a, 3)]
    for bits in product((0, 1), repeat=9):
        allowed = {d for d, bit in zip(range(-4, 5), bits) if bit}
        for source in intervals:
            for target in intervals:
                for q in range(1, 4):
                    assert direct_regular(source, target, allowed, q) == (
                        boundary_regular(source, target, allowed, q)
                    ), (list(source), list(target), q, allowed)
                    interval_cases += 1
    print(f"triangular indicator/modulus cases: {triangular_cases}")
    print(f"interval indicator/layer/modulus cases: {interval_cases}")


if __name__ == "__main__":
    main()
