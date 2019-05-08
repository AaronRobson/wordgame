import unittest

from wordgame import sort_words


class TestSortWords(unittest.TestCase):
    def test_empty(self):
        expected = []
        actual = list(sort_words([]))
        self.assertEqual(expected, actual)

    def test_singular(self):
        expected = ['a']
        actual = list(sort_words(['a']))
        self.assertEqual(expected, actual)

    def test_prefix(self):
        expected = [
            'leisurely',
            'aardvark',
            'idea',
            'word',
            'bad',
            'i',
        ]
        actual = list(sort_words([
            'i',
            'idea',
            'word',
            'aardvark',
            'bad',
            'leisurely',
        ]))
        self.assertEqual(expected, actual)
