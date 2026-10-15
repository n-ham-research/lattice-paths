import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import unittest
from itertools import product
from experiments.tree_bijections import (excursion_to_degrees, degrees_to_excursion,
                            excursion_to_dyck, dyck_to_excursion)


class TreeBijections(unittest.TestCase):
    def test_exhaustive_both_directions(self):
        # Independently enumerate all Dyck words, then test allowed ascents
        # against every subset of possible nonpositive step sizes.
        for n in range(8):
            images = set()
            for word in map(''.join, product('UD', repeat=2*n)):
                h = 0
                valid = True
                for ch in word:
                    h += 1 if ch == 'U' else -1
                    if h < 0:
                        valid = False
                        break
                if not valid or h:
                    continue
                path = dyck_to_excursion(word)
                self.assertEqual(len(path), n)
                self.assertEqual(excursion_to_dyck(path), word)
                self.assertEqual(degrees_to_excursion(excursion_to_degrees(path)), path)
                ascents = [len(s) for s in word.split('D') if s]
                self.assertEqual(sorted(ascents), sorted(1-s for s in path if s <= 0))
                images.add(path)
            # Different independent enumeration over bounded integer increments.
            paths = set()
            def visit(p, h):
                if len(p) == n:
                    if h == 0:
                        paths.add(tuple(p))
                    return
                for s in range(-h, 2):
                    visit(p+[s], h+s)
            visit([], 0)
            self.assertEqual(images, paths)

    def test_invalid_inputs(self):
        for path in ((-1, 1), (1,), (2, -2)):
            with self.assertRaises(ValueError):
                excursion_to_degrees(path)
        for degrees in ((), (0, 0), (2, 0), (-1,)):
            with self.assertRaises(ValueError):
                degrees_to_excursion(degrees)
