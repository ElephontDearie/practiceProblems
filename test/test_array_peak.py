import unittest
import os

from src.array_peak.array_peak_finder import find_peak


class ArrayPeakTest(unittest.TestCase):

    def test_finds_peak_from_scenario(self):
        input_array = [1, 3, 4, 5, 2, 1, 1]
        swap_operations = [[0, 1], [3, 4]]
        # 3, 1, 4, 5, 2, 1, 1  <- after 1st swap
        # 3, 1, 4, 2, 5, 1, 1  <- after 2nd swap
        actual = find_peak(input_array, swap_operations)
        self.assertEqual(actual, 4)
        