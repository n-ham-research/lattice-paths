"""Independent mathematical reference formulae, not fitted sequence identities."""
from math import factorial


def alternating(n):
    return sum((-1)**(n-k)*factorial(k) for k in range(1, n+1))


def balanced_factorials(n):
    return factorial(n//2)*factorial((n+1)//2)


def finite_difference_candidate(values):
    """Return the first constant difference order; a diagnostic, never a proof."""
    row = list(values)
    for order in range(len(row)):
        if len(row) >= 2 and len(set(row)) == 1:
            return order, row[0]
        row = [b-a for a, b in zip(row, row[1:])]
    return None
