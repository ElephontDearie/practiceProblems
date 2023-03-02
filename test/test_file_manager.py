import unittest
import os

from src.linked_list.linked_list import LinkedList
from src.linked_list.file_manager import FileManager


class FileManagerTest(unittest.TestCase):
    under_test = FileManager()

    def test_loads_small_file_correctly(self):
        result = self.under_test.load_file_as_string('test/data/small.txt')
        self.assertEqual(type(result), str)
        self.assertEqual(len(result.split("\n")), 3001)

    def test_loads_int_file_to_linked_list(self):
        result = self.under_test.load_to_linked_list('test/data/small.txt')
        self.assertEqual(type(result), LinkedList)
        self.assertEqual(result.head.value, 30253)
        self.assertEqual(result.next().value, 10425)
        self.assertEqual(result.next().value, 7576)
        self.assertEqual(result.next().value, 8233)
        self.assertEqual(result.next().value, 26029)
        

    def test_saves_reversed_to_file(self):
        input_dict = dict(enumerate([1, 2, 3, 4, 5, 6, 7]))
        initial_list = LinkedList(input_dict)
        self.under_test.save_reversed_to_file(initial_list, "test/data/test.txt")

        with open("test/data/test.txt") as f:
            first_line = f.readline()
            f.close()
            self.assertTrue(first_line == '7\n')
        os.remove("test/data/test.txt")


    def test_load_and_save_reversed_to_file(self):
        initial_list = self.under_test.load_to_linked_list('test/data/small.txt')
        self.under_test.save_reversed_to_file(initial_list, "test/data/test_small.txt")

        with open("test/data/test_small.txt") as f:
            first_line = f.readline()
            f.close()
            self.assertTrue(first_line == '22802\n')
        os.remove("test/data/test_small.txt")


    @unittest.skip("Not committing big files")
    def test_loads_medium_file_correctly(self):
        result = self.under_test.load_file_as_string('test/data/regular.txt')
        self.assertEqual(type(result), str)
        self.assertEqual(len(result.split("\n")), 3000001)
        

if __name__ == '__main__':
    unittest.main()