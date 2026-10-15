"""Exact finite checks for phase-3 weighted boundary graphs and q=1 cones."""
from itertools import product
from fractions import Fraction


def boundary_components(layers, q):
    vertices = {y-z for source, target in zip(layers, layers[1:])
                for z in source for y in target}
    parent = {x: x for x in vertices}
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for source, target in zip(layers, layers[1:]):
        for r in range(q):
            cell = [z for z in source if z % q == r]
            if not cell:
                continue
            for y in target:
                if y+q in target:
                    u, v = y-cell[0]+q, y-cell[-1]
                    parent[root(u)] = root(v)
    return {x: root(x) for x in vertices}


def direct_regular(layers, q, weights):
    for source, target in zip(layers, layers[1:]):
        for r in range(q):
            cell = [z for z in source if z % q == r]
            for s in range(q):
                sums = {sum((weights[y-z] for z in cell), Fraction(0))
                        for y in target if y % q == s}
                if len(sums) > 1:
                    return False
    return True


def verify():
    cases = 0
    intervals = [()] + [tuple(range(a,b+1)) for a in range(-1,2) for b in range(a,2)]
    for source, target in product(intervals, repeat=2):
        for q in range(1,4):
            layers = [source,target]
            graph = boundary_components(layers,q)
            vertices = sorted(graph)
            for values in product((Fraction(-1,2), Fraction(0), Fraction(2,3)), repeat=len(vertices)):
                weights = dict(zip(vertices,values))
                component_values = {}
                graph_regular = True
                for v in vertices:
                    c = graph[v]
                    if c in component_values and component_values[c] != weights[v]:
                        graph_regular = False
                    component_values[c] = weights[v]
                assert direct_regular(layers,q,weights) == graph_regular
                cases += 1
    cones = 0
    for a in range(-3,4):
        for k in range(1,9):
            for horizon in range(1,13):
                layers = [tuple(range(a*n,(a+k)*n+1)) for n in range(horizon+1)]
                graph = boundary_components(layers,1)
                assert set(graph) == set(range(a-k*(horizon-1),a+k*horizon+1))
                assert len(set(graph.values())) == 1
                cones += 1
    funnels = 0
    for widths in product(range(5), repeat=4):
        if tuple(sorted(widths)) != widths:
            continue
        layers = [tuple(range(s+1)) for s in (0,)+widths]
        graph = boundary_components(layers,1)
        assert len(set(graph.values())) == 1
        assert set(graph) == set(range(-widths[-2],widths[-1]+1))
        funnels += 1
    print(f'arbitrary widening funnel connectivity: {funnels} cases')
    print(f'weighted graph equivalence: {cases} exact rational cases; integer-cone connectivity: {cones} cases')


if __name__ == '__main__':
    verify()
