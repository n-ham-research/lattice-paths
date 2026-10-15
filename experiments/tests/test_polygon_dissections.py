import unittest
from experiments.polygon_dissections import (
    crossing, face_sizes, enumerate_even_dissections, parity_formula)
from experiments.table_audit import table_counts


class PolygonDissections(unittest.TestCase):
    def test_direct_geometry_against_formula_and_paths(self):
        ordinary, tested = enumerate_even_dissections(10)
        self.assertEqual(tested, 472)
        self.assertEqual(ordinary, {4: 1, 6: 1, 7: 3, 8: 1, 9: 8, 10: 13})
        paths = table_counts(4, 9, 0)
        for edges in range(2, 11):
            with self.subTest(edges=edges):
                self.assertEqual(ordinary.get(edges, 0), parity_formula(edges))
                self.assertEqual(ordinary.get(edges, 0), paths.get((edges-1, 0), 0))
        # Formal size one is separate from every ordinary polygon.
        self.assertNotIn(1, ordinary)
        self.assertEqual(parity_formula(1), 1)
        self.assertEqual(paths[(0, 0)], 1)

    def test_geometric_primitives(self):
        self.assertTrue(crossing((0, 3), (1, 4)))
        self.assertFalse(crossing((0, 3), (0, 4)))
        self.assertFalse(crossing((0, 4), (1, 3)))
        self.assertEqual(sorted(face_sizes(6, ((0, 3),))), [4, 4])
        self.assertEqual(sorted(face_sizes(6, ((0, 2), (0, 3)))), [3, 3, 4])
        self.assertEqual(sorted(face_sizes(6, ((0, 3), (0, 2)))), [3, 3, 4])
        for invalid in (0, -1, 1.5):
            with self.assertRaises(ValueError):
                parity_formula(invalid)
