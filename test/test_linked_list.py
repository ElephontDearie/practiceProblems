import unittest

from src.linked_list.linked_list import LinkedList
from src.linked_list.linked_node import LinkedNode

class LinkedListTest(unittest.TestCase):
    def test_is_a_linked_list(self):
        input_dict = dict(enumerate([1, 2, 3, 4, 5, 6, 7]))
        under_test = LinkedList(input_dict)
        self.assertTrue(type(under_test) == LinkedList)
        self.assertTrue(type(under_test.head) == LinkedNode)
    
    def test_creates_a_list_of_size_provided_parameter(self):
        input_dict = dict(enumerate([1, 2, 3]))
        under_test = LinkedList(input_dict)
        self.assertTrue(type(under_test.head) == LinkedNode)

        second_node = under_test.next()
        third_node = under_test.next()
        fourth_node = under_test.next()

        self.assertTrue(type(second_node) == LinkedNode)
        self.assertTrue(type(third_node) == LinkedNode)
        self.assertTrue(type(fourth_node) == type(None))

    
    def test_head_is_at_index(self):
        input_dict = dict(enumerate([1, 2, 3, 4, 5, 6, 7]))
        under_test = LinkedList(input_dict)
        self.assertEqual(under_test.head.value, 1)
        self.assertTrue(type(under_test.head) == LinkedNode)

    def test_pointers_in_between_node(self):
        input_dict = dict(enumerate([1, 2, 3, 4, 5, 6, 7]))
        under_test = LinkedList(input_dict)

        self.assertEqual(under_test.head.value, 1)
        self.assertEqual(under_test.next().value, 2)
        self.assertEqual(under_test.next().value, 3)
        self.assertEqual(under_test.next().value, 4)
        self.assertEqual(under_test.next().value, 5)
        self.assertEqual(under_test.next().value, 6)
        self.assertEqual(under_test.next().value, 7)




if __name__ == '__main__':
    unittest.main()