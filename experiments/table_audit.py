"""Recompute numeric facts from all ten original tables; no PDF needed to run."""
import json
from pathlib import Path
if __package__:
    from .lattice_paths import unit_columns
else:
    from lattice_paths import unit_columns


def table_counts(number, n, ymax):
    if number == 7:
        # At any intermediate time a path ending at height <=ymax in <=n
        # steps can have height at most ymax+n: every decrease is exactly 1.
        cap = ymax+n
        cols = unit_columns(n, lambda x: range(cap+1), lambda d: d == -1 or d > 0)
    elif number in (4,6):
        allowed = (lambda d: d == 1 or (d < 0 and d % 2 == 0)) if number == 4 else (lambda d: d == 1 or d < 0)
        cols = unit_columns(n, lambda x: range(x+1), allowed)
    else:
        def allowed_drop(a):
            return {1: a==2, 2: a==3, 3: a==4, 5: a%2==1,
                    8: True, 9: a%2==0, 10: a%3==0}[number]
        # Each upstep increases x by 1 and y by 1; vertical steps decrease y.
        # Therefore 0<=height<=x, and same-column descending order is acyclic.
        cols=[]
        for x in range(n+1):
            col={}
            for y in range(x,-1,-1):
                value=int(x==0 and y==0)
                if x:
                    value += cols[x-1].get(y-1,0)
                value += sum(col[z] for z in range(y+1,x+1) if allowed_drop(z-y))
                col[y]=value
            cols.append(col)
    return {(x,y):c for x,col in enumerate(cols) for y,c in col.items() if y<=ymax}


def check_tables():
    data=json.loads(Path(__file__).with_name('source_tables.json').read_text())
    checked=0
    differences=[]
    label_defects=[]
    for table in data['tables']:
        cells=table['cells']
        actual=table_counts(table['table'],max(c[0] for c in cells),max(c[1] for c in cells))
        for x,y,value in cells:
            checked+=1
            if actual.get((x,y),0)!=value:
                differences.append((table['table'],x,y,value,actual.get((x,y),0)))
        for x,label in enumerate(table['printed_x_labels']):
            if label!=x:
                label_defects.append((table['table'],x,label))
    return checked,differences,label_defects


if __name__ == '__main__':
    checked,differences,labels=check_tables()
    print(f'{checked} printed entries checked; value discrepancies: {differences}; axis-label defects: {labels}')
    if differences:
        raise SystemExit(1)
