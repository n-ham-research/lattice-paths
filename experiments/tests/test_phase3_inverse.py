import unittest
from fractions import Fraction
from itertools import product
from experiments.trajectory_inverse import endpoint_rows, recover_weights, residue_uniform
from experiments.phase3_geometry import direct_regular, boundary_components


class Phase3Inverse(unittest.TestCase):
    def test_explicit_words_and_inverse(self):
        f={-1:Fraction(1,2),0:Fraction(2),1:Fraction(1,3),2:Fraction(1,4)}
        rows=endpoint_rows(f,5)
        for n in range(6):
            explicit=[Fraction(0)]*(n+1)
            for word in product(f,repeat=n):
                h=0;weight=Fraction(1)
                for x,d in enumerate(word,1):
                    h+=d;weight*=f[d]
                    if not 0<=h<=x:
                        break
                else:
                    explicit[h]+=weight
            self.assertEqual(rows[n],explicit)
        self.assertEqual(recover_weights(rows),{d:f.get(d,0) for d in range(-4,6)})

    def test_data_and_horizon_counterexamples(self):
        f={d:1 for d in (-5,-3,0,1,4,6)}
        rows=endpoint_rows(f,7)
        self.assertTrue(all(residue_uniform(row,5) for row in rows[:7]))
        self.assertFalse(residue_uniform(rows[7],5))
        self.assertEqual(rows[6],[22,22,24,20,24,22,22])
        self.assertNotEqual(f.get(-4,0),f[1])
        self.assertEqual(endpoint_rows({0:1},8),endpoint_rows({d:1 for d in range(-8,1)},8))
        with self.assertRaises(ValueError):recover_weights([[1],[1]])
        with self.assertRaises(ValueError):recover_weights(endpoint_rows({0:1},2))
        with self.assertRaises(ValueError):recover_weights([[1],[1,1],[1,999,1]])

    def test_positive_characteristic_pivot_caveat(self):
        row=endpoint_rows({d:1 for d in (-1,0,1,2)},2)[2]
        self.assertEqual(row,[2,2,2])
        self.assertEqual([int(x)%2 for x in row],[0,0,0])

    def test_sharp_structural_and_geometric_obstructions(self):
        for q in range(3,9):
            layers=[tuple(range(n+1)) for n in range(q)]
            f={d:int(d==q-1) for d in range(2-q,q)}
            self.assertTrue(direct_regular(layers,q,f))
            self.assertNotEqual(f[-1],f[q-1])
        layers=[(0,),(0,1),(0,),(0,1),(0,)]
        f={-1:0,0:1,1:1}
        self.assertTrue(direct_regular(layers,1,f))
        self.assertEqual(len(set(boundary_components(layers,1).values())),2)
