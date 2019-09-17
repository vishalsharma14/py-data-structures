# Unit tests for Stack
import unittest

from data_structures import Stack
from data_structures import exceptions

STACK_SIZE_ZERO_MSG = "Stack should be empty"
INCORRECT_STACK_SIZE_MSG = "Incorrect stack size"


class StackTest(unittest.TestCase):

    def test_size(self):
        """
            Test Case to check the size of the stack after push and pop operations
        """
        stack = Stack()
        self.assertEqual(stack.length, 0, STACK_SIZE_ZERO_MSG)
        stack.push(1)
        self.assertEqual(stack.length, 1, INCORRECT_STACK_SIZE_MSG)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.length, 3, INCORRECT_STACK_SIZE_MSG)
        stack.pop()
        self.assertEqual(stack.length, 2, INCORRECT_STACK_SIZE_MSG)

    def test_push(self):
        """
            Test Case to test the push operation
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.top, 1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top, 3)

    def test_pop(self):
        """
            Test Case to test the pop operation
        """
        stack = Stack()
        stack.push(1)
        num = stack.pop()
        self.assertEqual(num, 1)
        stack.push(2)
        stack.push(3)
        num = stack.pop()
        self.assertEqual(num, 3)

    def test_pop_on_empty_stack(self):
        """
            Test Case to test pop operation on Empty Stack
        """
        stack = Stack()
        stack.push(1)
        stack.pop()
        self.assertEqual(stack.length, 0, STACK_SIZE_ZERO_MSG)

        # Stack should be empty after one push and one pop operation
        # Should raise EmptyStackException on pop()
        with self.assertRaises(exceptions.EmptyStackException):
            stack.pop()

    def test_top(self):
        """
            Test Case to test top property
        """
        stack = Stack()
        stack.push(1)
        top_item = stack.top
        self.assertEqual(top_item, 1)

        stack.push(4)
        self.assertEqual(stack.length, 2, INCORRECT_STACK_SIZE_MSG)
        top_item = stack.top
        self.assertEqual(top_item, 4)

        # Top should not pop() the top most item
        # Stack size remains same after top
        self.assertEqual(stack.length, 2, INCORRECT_STACK_SIZE_MSG)

    def test_top_on_empty_stack(self):
        """
            Test Case to test top property on Empty Stack
        """
        stack = Stack()
        stack.push(1)
        top_item = stack.top
        self.assertEqual(top_item, 1)
        self.assertEqual(stack.length, 1)

        stack.pop()

        self.assertEqual(stack.length, 0, STACK_SIZE_ZERO_MSG)

        # Should raise EmptyStackException on top on empty stack
        with self.assertRaises(exceptions.EmptyStackException):
            stack.top


if __name__ == '__main__':
    unittest.main()
