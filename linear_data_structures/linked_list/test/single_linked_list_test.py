# tests/test_linked_list.py

import unittest
from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_beginning(self):
        self.ll.insert_at_beginning(10)
        self.assertEqual(self.ll.get_at_position(0), 10)
        self.ll.insert_at_beginning(20)
        self.assertEqual(self.ll.get_at_position(0), 20)
        self.assertEqual(self.ll.get_at_position(1), 10)

    def test_insert_at_end(self):
        self.ll.insert_at_end(30)
        self.assertEqual(self.ll.get_at_position(0), 30)
        self.ll.insert_at_end(40)
        self.assertEqual(self.ll.get_at_position(1), 40)

    def test_insert_at_position(self):
        self.ll.insert_at_end(50)
        self.ll.insert_at_position(1, 60)
        self.assertEqual(self.ll.get_at_position(1), 60)
        self.ll.insert_at_position(0, 70)
        self.assertEqual(self.ll.get_at_position(0), 70)

    def test_delete_from_beginning(self):
        self.ll.insert_at_end(80)
        self.ll.insert_at_end(90)
        self.ll.delete_from_beginning()
        self.assertEqual(self.ll.get_at_position(0), 90)

    def test_delete_from_end(self):
        self.ll.insert_at_end(100)
        self.ll.insert_at_end(110)
        self.ll.delete_from_end()
        self.assertEqual(self.ll.get_at_position(0), 100)

    def test_get_at_position(self):
        self.ll.insert_at_end(120)
        self.ll.insert_at_end(130)
        self.assertEqual(self.ll.get_at_position(1), 130)

    def test_size(self):
        self.assertEqual(self.ll.size(), 0)
        self.ll.insert_at_end(140)
        self.assertEqual(self.ll.size(), 1)
        self.ll.insert_at_end(150)
        self.assertEqual(self.ll.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.ll.is_empty())
        self.ll.insert_at_end(160)
        self.assertFalse(self.ll.is_empty())

    def test_delete_at_position(self):
        self.ll.insert_at_end(170)
        self.ll.insert_at_end(180)
        self.ll.insert_at_end(190)
        self.ll.delete_at_position(1)
        self.assertEqual(self.ll.get_at_position(1), 190)

    def test_print_list(self):
        import io
        import sys
        buffer = io.StringIO()
        sys.stdout = buffer
        self.ll.insert_at_end(200)
        self.ll.insert_at_end(210)
        self.ll.print_list()
        sys.stdout = sys.__stdout__
        output = buffer.getvalue().strip()
        self.assertEqual(output, "200 -> 210 -> None")


if __name__ == "__main__":
    unittest.main()
