import unittest

from src.binary_search.index import get_square_root

class SquareRootFinderTest(unittest.TestCase):

    def test_works_for_whole_nums(self):
        actual = get_square_root(4)
        # print("\n")
        # print(actual)
        self.assertAlmostEqual(actual, 2.000000, places = 6)

    def test_works_for_25(self):
        actual = get_square_root(25)
        self.assertEqual(actual, 5)