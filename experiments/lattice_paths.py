"""Exact finite DAG counting, with an adapter for unit-horizontal lattice paths.

Infinite step sets are membership predicates evaluated only on finite vertex pairs.
The caller must prove that its finite induced DAG captures the intended paths.
"""
from collections import defaultdict


def dag_counts(vertices, edge, start=(0, 0)):
    """Count paths on distinct topologically ordered vertices; reject backward edges.

    Edge is a boolean relation: parallel edges are intentionally unsupported.
    O(V^2) predicate calls; arbitrary-precision integer counts.
    """
    vertices = tuple(vertices)
    if len(set(vertices)) != len(vertices) or start not in vertices:
        raise ValueError('Vertices must be distinct and contain start')
    for i, u in enumerate(vertices):
        if any(edge(u, v) for v in vertices[:i+1]):
            raise ValueError('Self-loop or non-topological edge')
    counts = {v: 0 for v in vertices}
    counts[start] = 1
    for i, v in enumerate(vertices):
        counts[v] += sum(counts[u] for u in vertices[:i] if edge(u, v))
    return counts


def _heights(heights, x):
    values = tuple(heights(x))
    if len(values) != len(set(values)):
        raise ValueError("Region heights must be distinct")
    return values


def unit_columns(n, heights, allowed):
    """Counts through column n; heights(x) must describe the FULL finite region.

    All steps have dx=1; allowed(dy) tests step membership. Endpoints outside
    heights are forbidden throughout the path, not merely at its end.
    """
    if n < 0:
        raise ValueError('Negative column')
    columns = [{0: 1}]
    if 0 not in _heights(heights, 0):
        raise ValueError('Origin outside region')
    for x in range(1, n+1):
        columns.append({y: sum(c for z, c in columns[-1].items() if allowed(y-z))
                        for y in _heights(heights, x)})
    return columns


def explicit_paths(n, heights, allowed):
    """Generate actual height tuples, for SMALL unit-column problems only."""
    if n < 0 or 0 not in _heights(heights, 0):
        raise ValueError('Invalid domain')
    def extend(path):
        x = len(path)
        if x == n+1:
            yield path
            return
        for y in _heights(heights, x):
            if allowed(y-path[-1]):
                yield from extend(path+(y,))
    yield from extend((0,))


def aggregate(counts, key):
    """Sum a finite endpoint-count mapping by any row/column/diagonal key."""
    result = defaultdict(int)
    for point, count in counts.items():
        result[key(point)] += count
    return dict(result)


def model(name):
    regions = {'triangle': lambda x: range(x+1),
               'cone': lambda x: range(-x, x+1)}
    specs = {'24-all': ('triangle', lambda d: True),
             '24-odd': ('cone', lambda d: d % 2 != 0),
             '24-nonzero': ('triangle', lambda d: d != 0),
             '26-nonzero': ('cone', lambda d: d != 0),
             '27-odd': ('triangle', lambda d: d % 2 != 0),
             '27-even': ('triangle', lambda d: d % 2 == 0)}
    region, step = specs[name]
    return regions[region], step
