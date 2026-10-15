"""Independent path-word checks for generalized inverse enumeration."""
import sys
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from phase4_inverse import funnel_rows, recover_funnel


class FunnelInverseTests(unittest.TestCase):
    def test_words_and_corner_reconstruction_with_width_jumps(self):
        widths=(0,0,2,2,4)
        f={d:Fraction(abs(d)+1,3) for d in range(-2,5)}
        expected=[[Fraction(1)]]
        for n in range(1,len(widths)):
            row=[Fraction(0)]*(widths[n]+1)
            for word in product(f,repeat=n):
                height=0
                weight=Fraction(1)
                for layer,d in enumerate(word,1):
                    height+=d
                    if not 0<=height<=widths[layer]:
                        break
                    weight*=f[d]
                else:
                    row[height]+=weight
            expected.append(row)
        self.assertEqual(funnel_rows(f,widths),expected)
        self.assertEqual(recover_funnel(expected,widths),f)

    def test_invalid_dimensions_zero_pivot_and_inconsistent_data(self):
        with self.assertRaises(ValueError):
            recover_funnel([[1],[1]],(0,1))
        with self.assertRaises(ValueError):
            recover_funnel([[1],[0,1],[0,0,0]],(0,1,2))
        rows=funnel_rows({d:1 for d in range(-2,4)},(0,1,2,3))
        rows[-1][1]+=1
        with self.assertRaises(ValueError):
            recover_funnel(rows,(0,1,2,3))
