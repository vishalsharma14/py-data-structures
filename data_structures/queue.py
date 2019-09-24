from collections import deque
from data_structures.exceptions import EmptyQueueException


class Queue(object):

    def __init__(self):
        self._elements = deque()

    @property
    def length(self):
        """
            Returns length of the queue
        """
        return len(self._elements)

    def enqueue(self, item):
        """
            Adds an item at the end of queue
            :param item: Item to be appended
        """
        self._elements.append(item)

    @property
    def last_item(self):
        """
            If Queue is not empty: returns last item
            else: raise EmptyQueueException
        """
        if self.length > 0:
            return self._elements[-1]
        raise EmptyQueueException

    @property
    def first_item(self):
        """
            If Queue is not empty: returns first item
            else: raise EmptyQueueException
        """
        if self.length > 0:
            return self._elements[0]
        raise EmptyQueueException

    def dequeue(self):
        """
            Pops an item from the start of queue
        """
        if self.length <= 0:
            raise EmptyQueueException
        return self._elements.popleft()

    def iterate(self):
        """
            override to perform an operation on the queue
        """
        return self
