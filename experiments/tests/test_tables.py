import unittest
from experiments.table_audit import check_tables, table_counts


class SourceTables(unittest.TestCase):
    def test_all_printed_entries(self):
        count,differences,labels=check_tables()
        self.assertEqual(count,697)
        self.assertEqual(differences,[])
        self.assertEqual(labels,[(6,13,12),(7,13,12)])

    def test_vertical_explicit_words(self):
        # Independent actual word enumeration; total x budget strictly bounds
        # upsteps, and downward steps strictly decrease nonnegative height.
        for number,drop in ((1,lambda a:a==2),(5,lambda a:a%2==1),
                            (8,lambda a:True),(10,lambda a:a%3==0)):
            for n in range(5):
                actual={}
                def visit(x,y,word):
                    if x==n:
                        actual[y]=actual.get(y,0)+1
                    if x<n:
                        visit(x+1,y+1,word+((1,1),))
                    for a in range(1,y+1):
                        if drop(a):
                            visit(x,y-a,word+((0,-a),))
                visit(0,0,())
                counts=table_counts(number,n,n)
                self.assertEqual({y:counts.get((n,y),0) for y in range(n+1)},
                                 {y:actual.get(y,0) for y in range(n+1)})

    def test_axis_specializations(self):
        from math import comb
        from experiments.lattice_paths import unit_columns
        # Independent closed coefficients (Lagrange inversion) versus path DP.
        for m,number in ((2,1),(3,2),(4,3)):
            cols=table_counts(number,5*m,5*m)
            for n in range(6):
                expected=comb((m+1)*n,n)//(m*n+1)
                self.assertEqual(cols.get((m*n,0),0),expected)
                allowed=lambda d: d==1 or (1-d>=m and (1-d)%m==0)
                self.assertEqual(unit_columns(m*n,lambda x:range(x+1),allowed)[-1][0],expected)
        for m,number in ((1,8),(2,9),(3,10)):
            cols=table_counts(number,6*m,6*m)
            for n in range(1,7):
                expected=sum(comb(n,j)*2**j*comb(m*n,n-1-j) for j in range(n))//n
                self.assertEqual(cols.get((m*n,0),0),expected)
        large=[1]
        for n in range(1,11):
            large.append(large[-1]+sum(large[j]*large[n-1-j] for j in range(n)))
        cols=table_counts(8,10,10)
        self.assertEqual([cols[(n,0)] for n in range(11)], [1]+[v//2 for v in large[1:]])
