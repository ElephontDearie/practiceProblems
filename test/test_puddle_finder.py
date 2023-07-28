import unittest
from src.graph.index import find_puddle


class PuddleTest(unittest.TestCase):

    def test_finds_puddle_from_scenario(self):
        input_array = ["###.#", "..#..", ".#.##", "#####"]
        actual = find_puddle(input_array)
        self.assertEqual(actual, 3)