# Unit tests for Queue
import unittest
from data_structures import Queue
from data_structures import exceptions


QUEUE_LENGTH_ZERO = 0


class QueueTest(unittest.TestCase):

    def test_queue_size_on_initialization(self):
        queue = Queue()
        self.assertEqual(queue.length, QUEUE_LENGTH_ZERO)

    def test_queue_size_on_first_enqueue_operation(self):
        queue = Queue()
        queue.enqueue(2)

        self.assertEqual(queue.length, 1)

    def test_queue_size_on_multiple_enqueue_operation(self):
        queue = Queue()
        items = [3, 4, 5, 7, 9, 101, "abcd", "This is an item"]

        for item in items:
            queue.enqueue(item)

        self.assertEqual(queue.length, len(items))

    def test_last_item_on_first_item_enqueue(self):
        queue = Queue()
        item = 3
        queue.enqueue(item)

        self.assertEqual(queue.last_item, item)

    def test_last_item_on_subsequent_item_enqueue(self):
        queue = Queue()

        items = [3, 4, 1, 111, "abcd", "This is an item"]

        for item in items:
            queue.enqueue(item)
            self.assertEqual(queue.last_item, item)

    def test_exception_on_last_item_on_empty_queue(self):
        queue = Queue()

        with self.assertRaises(exceptions.EmptyQueueException):
            queue.last_item
