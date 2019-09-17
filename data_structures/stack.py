
from data_structures.exceptions import EmptyStackException


class Stack:

    def __init__(self):
        self.stack = []

    @property
    def length(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.length > 0:
            return self.stack.pop()
        else:
            raise EmptyStackException
