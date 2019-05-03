import unittest

import wordgame

_WORDS = [
    'bad',
]


class TestCountdown(unittest.TestCase):
    def test(self):
        actual = list(wordgame.countdown('abcd', words=_WORDS))
        expected = ['bad']
        self.assertEqual(actual, expected)


class TestCanWordBeMadeWithLetters(unittest.TestCase):
    def test(self):
        self.assertTrue(wordgame._can_word_be_made_with_letters(word='bad', letters='abcd'))
