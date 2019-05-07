import unittest

from wordgame.__main__ import take


class TestTake(unittest.TestCase):
    def test_number_of_None(self):
        expected = [0, 1, 2]
        actual = list(take(None, range(3)))
        self.assertEqual(actual, expected)

    def test_number_of_zero(self):
        expected = []
        actual = list(take(0, range(3)))
        self.assertEqual(actual, expected)

    def test_number_same(self):
        expected = [0, 1, 2]
        actual = list(take(3, range(3)))
        self.assertEqual(actual, expected)

    def test_number_smaller(self):
        expected = [0, 1]
        actual = list(take(2, range(3)))
        self.assertEqual(actual, expected)

    def test_number_larger(self):
        expected = [0, 1, 2]
        actual = list(take(5, range(3)))
        self.assertEqual(actual, expected)

    def test_number_negative(self):
        expected = []
        actual = list(take(-1, range(3)))
        self.assertEqual(actual, expected)
