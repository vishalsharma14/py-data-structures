
from data_structures.exceptions import EmptyStackException


class Stack(object):
    """
        Class representing Stack Data Structure (LIFO)
    """

    def __init__(self):
        self._elements = []

    @property
    def length(self):
        """
            :return: Length of the Stack
        """
        return len(self._elements)

    @property
    def top(self):
        """
            Checks and returns the top item from the stack
            :return: EmptyStackException if stack is empty
                else Top item
        """
        if self.length > 0:
            return self._elements[-1]
        else:
            raise EmptyStackException

    def push(self, item):
        """
            Pushes an element in the stack
            :param item: Item to be inserted
        """
        self._elements.append(item)

    def pop(self):
        """
            Pops the top item from the stack
            :return: EmptyStackException if stack is empty
                else Top item
        """
        if self.length > 0:
            return self._elements.pop()
        else:
            raise EmptyStackException

    def iterate(self):
        """
            override to perform an operation on the stack
        """
        return self
