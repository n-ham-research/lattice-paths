"""Explicit classical excursion/preorder-degree/Dyck bijection; no external code."""

def excursion_to_degrees(path):
    path = tuple(path)
    height = 0
    for step in path:
        if not isinstance(step, int) or step > 1:
            raise ValueError('steps must be integers at most one')
        height += step
        if height < 0:
            raise ValueError('negative prefix')
    if height:
        raise ValueError('not an excursion')
    return tuple(1 - s for s in reversed(path)) + (0,)


def degrees_to_excursion(degrees):
    degrees = tuple(degrees)
    slots = 1
    for d in degrees:
        if slots <= 0 or not isinstance(d, int) or d < 0:
            raise ValueError('invalid preorder degrees')
        slots += d - 1
    if slots != 0:
        raise ValueError('incomplete tree')
    return tuple(1 - d for d in reversed(degrees[:-1]))


def excursion_to_dyck(path):
    return ''.join('U' * d + 'D' for d in excursion_to_degrees(path))[:-1]


def dyck_to_excursion(word):
    height = 0
    for letter in word:
        if letter not in 'UD':
            raise ValueError('invalid letter')
        height += 1 if letter == 'U' else -1
        if height < 0:
            raise ValueError('negative prefix')
    if height:
        raise ValueError('not a Dyck word')
    return degrees_to_excursion(tuple(len(block) for block in (word + 'D').split('D')[:-1]))
