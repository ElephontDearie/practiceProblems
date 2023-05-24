import unittest

from src.binary_search.index import get_square_root

class SquareRootFinderTest(unittest.TestCase):

    def test_works_for_whole_nums(self):
        actual = get_square_root(4, [0, 4])
        self.assertAlmostEqual(actual, 2.000000, places = 6)

    def test_works_for_25(self):
        actual = get_square_root(25, [0, 25])
        self.assertAlmostEqual(actual, 5.000000, places = 6)

    def test_works_for_pi(self):
        pi = 3.14159265359
        actual = get_square_root(pi, [0, pi])
        self.assertAlmostEqual(actual, 1.772454, places = 6)