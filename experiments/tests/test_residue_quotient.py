import unittest
from experiments.lattice_paths import unit_columns


class ResidueQuotient(unittest.TestCase):
    def test_present_and_absent_cells(self):
        for q in range(1,5):
            for mask in range(2**q):
                allowed=lambda d:bool(mask&(1<<(d%q)))
                dp=unit_columns(8,lambda n:range(n+1),allowed)
                p=[1]+[0]*(q-1)
                for n in range(1,9):
                    oldsizes=[sum(z%q==r for z in range(n)) for r in range(q)]
                    p=[sum(oldsizes[r]*p[r]*allowed(s-r) for r in range(q)) if s<=n else 0 for s in range(q)]
                    for y,count in dp[n].items():
                        self.assertEqual(count,p[y%q])
                    for s in range(n+1,q):
                        self.assertEqual(p[s],0)
