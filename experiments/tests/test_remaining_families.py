import unittest
from functools import lru_cache
from itertools import product
from math import comb, factorial, prod
from experiments.remaining_families import sparse_down, residue_endpoint, arbitrary_positive_x, finite_progress


class RemainingFamilies(unittest.TestCase):
    def test_sparse_against_words(self):
        for q in range(1,5):
            for n in range(1,6):
                counts={}
                for ks in product(range(4),repeat=n):
                    # Restrict deficit to <=3: no removed word can contribute.
                    if sum(ks)<=3:
                        y=n-q*sum(ks)
                        counts[y]=counts.get(y,0)+1
                for k in range(4):
                    self.assertEqual(counts.get(n-q*k,0),sparse_down(n,n-q*k,q))

    def test_residue_against_endpoint_dp(self):
        for q in range(1,7):
            for wedge in (False,True):
                layer={0:1}
                for n in range(13):
                    self.assertEqual(set(layer.values()),{residue_endpoint(n,q,wedge)})
                    lo=-n-1 if wedge else 0
                    layer={y:sum(layer.values()) for y in range(lo,n+2) if y%q==0}
        for q in range(1,7):
            for n in range(13):
                self.assertEqual(residue_endpoint(n,q),prod(factorial((n+i)//q) for i in range(q)))

    def test_arbitrary_progress_against_explicit_words(self):
        for increments in ((-1,1),(-1,0,1),(0,1)):
            for vertical in (False,True):
                for target_x in range(5):
                    for target_y in range(-2,4):
                        # Direct words, with an endpoint-derived upper height bound.
                        @lru_cache(None)
                        def words(x,y):
                            if x>target_x or y>target_y+(target_x-x):
                                return 0
                            answer=int((x,y)==(target_x,target_y))
                            if vertical:
                                answer+=words(x,y+1)
                            for a in range(1,target_x-x+1):
                                for b in increments:
                                    answer+=words(x+a,y+b)
                            return answer
                        self.assertEqual(words(0,0),arbitrary_positive_x(target_x,target_y,increments,vertical))

    def test_unrestricted_bridge_gf(self):
        for n in range(16):
            direct = 1 if n==0 else sum(comb(n,k)*comb(n-k-1,k-1) for k in range(1,n//2+1))
            central_trinomial = sum(comb(n,2*k)*comb(2*k,k) for k in range(n//2+1))
            self.assertEqual(direct,(central_trinomial+(-1)**n)//2)

    def test_retained_counterexamples(self):
        finite=[(1,0),(1,1),(2,1),(3,1),(1,-1),(1,-2),(1,-3)]
        cols=finite_progress(3,finite)
        self.assertEqual((cols[3][1],cols[3][-1]),(9,17))
        for inc,upper in [((-1,0,1),6),((-1,1),4)]:
            self.assertEqual(arbitrary_positive_x(1,1,inc,True),upper)
            self.assertEqual(arbitrary_positive_x(1,-1,inc,True),1)
        self.assertEqual(sparse_down(2,0,2),2)

    def test_delannoy_difference(self):
        d=[sum(comb(n,k)*comb(n+k,k) for k in range(n+1)) for n in range(13)]
        expected=[1]+[d[n]-d[n-1] for n in range(1,13)]
        self.assertEqual([arbitrary_positive_x(n,0,(-1,1),True) for n in range(13)],expected)
