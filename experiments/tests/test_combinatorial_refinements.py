import unittest
from itertools import product
from collections import Counter
from experiments.combinatorial_refinements import (profile_count, vertical_multiple_count,
    packed_literature_count, sylvester_classes)


class CombinatorialRefinements(unittest.TestCase):
    def test_all_profiles_through_seven_steps(self):
        # Independent step-word enumeration, including horizontal steps.
        for n in range(8):
            counts = Counter()
            def visit(w,h):
                if len(w)==n:
                    if h==0:
                        counts[tuple(sorted(Counter(-s for s in w if s<=0).items()))]+=1
                    return
                for s in range(-h,2):
                    visit(w+(s,),h+s)
            visit((),0)
            for p,c in counts.items():
                self.assertEqual(profile_count(dict(p)),c)

    def test_direct_congruence(self):
        cases = [(m,n) for m in range(1,5) for n in range(4) if m*n<=8]
        cases += [(1,4),(1,5)]
        for m,n in cases:
            self.assertEqual(sylvester_classes(m,n),vertical_multiple_count(m,n),(m,n))

    def test_two_independent_finite_formulas(self):
        for m in range(1,9):
            for n in range(21):
                self.assertEqual(packed_literature_count(m,n),vertical_multiple_count(m,n))
