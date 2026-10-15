"""Exact widening-funnel inversion and labelled/unlabelled observation checks."""
from fractions import Fraction
from itertools import combinations_with_replacement, product


def funnel_rows(weights, widths):
    if widths[0] != 0 or any(a>b for a,b in zip(widths,widths[1:])):
        raise ValueError('Widths must start at zero and be nondecreasing')
    rows = [[Fraction(1)]]
    for width in widths[1:]:
        rows.append([sum((v*weights.get(y-z,0) for z,v in enumerate(rows[-1])), Fraction(0))
                     for y in range(width+1)])
    return rows


def recover_funnel(rows, widths):
    """Invert complete labelled rows, conditional on both edge pivots."""
    if not rows or not widths or len(rows)!=len(widths) or widths[0]!=0 or rows[0]!=[1]:
        raise ValueError('Invalid initial row or dimensions')
    if any(a>b for a,b in zip(widths,widths[1:])):
        raise ValueError('Nonmonotone widths')
    if any(len(row)!=s+1 for row,s in zip(rows,widths)):
        raise ValueError('Wrong row length')
    if len(rows)==1:
        return {}
    f = {d:Fraction(rows[1][d]) for d in range(widths[1]+1)}
    for n in range(2,len(rows)):
        a,b,c = widths[n-2:n+1]
        prev = rows[n-1]
        if not prev[0] or not prev[-1]:
            raise ValueError('Zero edge pivot')
        for y in range(b-a-1,-1,-1):
            d=y-b
            f[d]=(rows[n][y]-sum(prev[z]*f[y-z] for z in range(b)))/prev[b]
        for y in range(b+1,c+1):
            f[y]=(rows[n][y]-sum(prev[z]*f[y-z] for z in range(1,b+1)))/prev[0]
    if funnel_rows(f,widths)!=rows:
        raise ValueError('Inconsistent data')
    return f


def verify():
    funnels=0
    for tail in combinations_with_replacement(range(5),4):
        widths=(0,)+tail
        f={d:Fraction(abs(d)+2,abs(d)+3) for d in range(-widths[-2],widths[-1]+1)}
        rows=funnel_rows(f,widths)
        assert recover_funnel(rows,widths)==f
        # Constant kernels force the predicted scalar-uniform trajectory.
        alpha=Fraction(2,3)
        constant={d:alpha for d in f}
        current=Fraction(1)
        for n,row in enumerate(funnel_rows(constant,widths)):
            if n:
                current*=alpha*(widths[n-1]+1)
            assert row==[current]*(widths[n]+1)
        funnels+=1
    reflection=0
    widths=tuple(range(5))
    for bits in product((0,1),repeat=8):
        f=dict(zip(range(-3,5),bits))
        reflected={1-d:v for d,v in f.items()}
        rows=funnel_rows(f,widths)
        other=funnel_rows(reflected,widths)
        assert other==[row[::-1] for row in rows]
        assert [sorted(row) for row in rows]==[sorted(row) for row in other]
        reflection+=1
    # Genuine hidden predecessor data yield nonlinear, not affine, constraints.
    f={0:2,1:3,-1:5}
    assert funnel_rows(f,(0,1,2))[2][0]==2**2+3*5
    return {'monotone_funnel_inverse_cases':funnels,
            'constant_funnel_formula_cases':funnels,
            'binary_reflection_cases':reflection,
            'nonlinear_partial_observation_examples':1}


if __name__=='__main__':
    print(verify())
