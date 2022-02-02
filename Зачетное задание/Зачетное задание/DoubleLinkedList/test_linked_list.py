import unittest

from task import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_del_tail(self):
        ll = LinkedList([1, 2, 3])

        del ll[len(ll) - 1]

        self.assertEqual(2, len(ll))
        self.assertEqual(1, ll._head.value)
        self.assertEqual(2, ll._tail.value)
        """тест"""
    