import unittest

from src.linked_list.linked_node import LinkedNode

class LinkedNodeTest(unittest.TestCase):
    def test_is_a_linked_node(self):
        under_test = LinkedNode(1, None)
        self.assertTrue(type(under_test) == LinkedNode)
    
    def test_does_not_create_node_when_value_not_int(self):
        with self.assertRaises(TypeError):
            LinkedNode(None, None)
    
    def test_creates_node_when_value_is_int(self):
        under_test = LinkedNode(5, None)
        self.assertTrue(type(under_test) == LinkedNode)
        self.assertEqual(under_test.value, 5)
    
    def test_throws_exception_when_pointer_not_null_or_linkedNode_types(self):
        with self.assertRaises(TypeError):
            LinkedNode(5, 5)


if __name__ == '__main__':
    unittest.main()