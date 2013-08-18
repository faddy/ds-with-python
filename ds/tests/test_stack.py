import unittest
from data_structures.stacks import Stack


class TestStackStructure(unittest.TestCase):
    '''
    Test for:
    1. instantiating the Stack worked
    2. is_empty() works
    3. size() works
    4. push:
	- does not push None values
        - check size() when item is pushed
    5. pop:
	- does nothing when stack is empty
	- pops item in lifo manner
    6. peek:
	- push an item and check if peek() gives us the same item
    '''

    def setUp(self):
        self.seq = range(5)
        self.stack = Stack()

    def test_stack_creation(self):
        self.assertIsInstance(self.stack, Stack)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_empty_stack_size_is_zero(self):
        self.assertEqual(self.stack.size(), 0)

    def test_push_method(self):
        self.stack.push(None)
        self.assertEqual(self.stack.size(), 0)
        self.stack.push([])
        self.assertEqual(self.stack.size(), 1)

    def test_peek_method(self):
        self.assertEqual(self.stack.peek(), None)
        self.stack.push(5)
        self.stack.push(6)
        self.assertEqual(self.stack.peek(), 6)

    def test_pop_method(self):
        self.assertEqual(self.stack.pop(), None)
        for i in self.seq:
            self.stack.push(i)

        for i in reversed(self.seq):
            self.assertEqual(self.stack.pop(), i)


if __name__ == '__main__':
    unittest.main()
