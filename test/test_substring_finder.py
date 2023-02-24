from src.substring.substring import SubstringFinder
import unittest

class SubstringFinderTest(unittest.TestCase):
    # under_test = SubstringFinder()

    def test_gets_longest_substring(self):
        input_str_1 = "abcabcbb"
        input_str_2 = "pwwkew"

        actual_1 = SubstringFinder(input_str_1).longest_substring
        actual_2 = SubstringFinder(input_str_2).longest_substring

        self.assertEqual(actual_1, "abc")
        self.assertEqual(actual_2, "wke")

    def test_gets_longest_substring_when_repeated_chars(self):
        input_str = "bbbbb"
        actual = SubstringFinder(input_str).longest_substring
        self.assertEqual(actual, "b")


    def test_gets_longest_substring_when_before_repeated_char(self):
        input_str = "abcdaefgh"
        actual = SubstringFinder(input_str).longest_substring
        self.assertEqual(actual, "bcdaefgh")

    def test_gets_longest_substring_when_after_repeated_char(self):
        input_str = "abcdfeefghiklopz"
        actual = SubstringFinder(input_str).longest_substring
        self.assertEqual(actual, "efghiklopz")
    
    def test_gets_longest_substring_when_thrice_repeated_char(self):
        input_str = "aaaaaaabaca"
        actual = SubstringFinder(input_str).longest_substring
        self.assertEqual(actual, "bac")


