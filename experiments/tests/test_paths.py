import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import unittest
from collections import Counter
from math import comb, factorial
from lattice_paths import unit_columns, explicit_paths, dag_counts, aggregate, model
from sequences import alternating, balanced_factorials


class Paths(unittest.TestCase):
    def test_explicit_vs_dp(self):
        for name in ('24-all', '24-odd', '24-nonzero', '26-nonzero', '27-odd', '27-even'):
            h, s = model(name)
            for n in range(6):
                actual = Counter(p[-1] for p in explicit_paths(n, h, s))
                self.assertEqual(dict(actual), {y:c for y,c in unit_columns(n,h,s)[-1].items() if c})

    def test_formulas(self):
        for n in range(13):
            for name in ('24-all', '24-odd', '24-nonzero', '26-nonzero', '27-odd', '27-even'):
                h,s = model(name)
                c = unit_columns(n,h,s)[-1]
                if name == '24-all':
                    self.assertTrue(all(v == factorial(n) for v in c.values()))
                if name == '24-odd':
                    self.assertTrue(all(v == (factorial(n) if (n-y)%2 == 0 else 0) for y,v in c.items()))
                if name == '24-nonzero':
                    self.assertEqual(sum(c.values()), factorial(n))
                    if n:
                        self.assertEqual(c[n], factorial(n-1))
                        self.assertEqual(c[0], alternating(n-1))
                if name == '26-nonzero':
                    self.assertEqual(sum(c.values()), 2**n*factorial(n))
                    if n:
                        self.assertEqual(c[n], 2**(n-1)*factorial(n-1))
                if name.startswith('27-'):
                    residue = n%2 if name == '27-odd' else 0
                    self.assertTrue(all(v == (balanced_factorials(n) if y%2 == residue else 0) for y,v in c.items()))

    def test_catalan_and_vertical_dag(self):
        for n in range(7):
            vertices = sorted(((x,y) for x in range(2*n+1) for y in range(x+1)), key=lambda p:(p[0],-p[1]))
            c = dag_counts(vertices, lambda u,v: (v[0]-u[0],v[1]-u[1]) in {(1,1),(0,-1)})
            for k in range(n+1):
                self.assertEqual(c[(k,0)], comb(2*k,k)//(k+1))
        with self.assertRaises(ValueError):
            dag_counts([(0,0),(1,0)], lambda u,v: True)

    def test_verification_entry_points(self):
        import subprocess
        root = Path(__file__).resolve().parents[2]
        for args in (("-m", "experiments.verify", "--check"),
                     ("experiments/verify.py", "--check")):
            result = subprocess.run([sys.executable, *args], cwd=root,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_duplicate_region_is_rejected(self):
        h = lambda x: [0] if x == 0 else [0,0]
        with self.assertRaises(ValueError):
            unit_columns(1,h,lambda d: True)
        with self.assertRaises(ValueError):
            list(explicit_paths(1,h,lambda d: True))

    def test_aggregations(self):
        self.assertEqual(aggregate({(0,0):1,(1,0):2,(1,1):3},lambda p:p[0]),{0:1,1:5})
        self.assertEqual(unit_columns(5,lambda x:[0],lambda d:d==0)[-1],{0:1})

if __name__ == '__main__':
    unittest.main()
