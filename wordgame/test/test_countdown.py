import unittest
from unittest.mock import patch

import wordgame

_WORDS = [
    'bad',
    'rejoiced',
    'swearing',
]


class TestCountdown(unittest.TestCase):
    def test_simple(self):
        actual = list(wordgame.countdown('abcd', words=_WORDS))
        expected = 'bad'
        self.assertIn(expected, actual)

    def test_swearing(self):
        '''featured in 8 out 10 cats does Countdown'''
        actual = list(wordgame.countdown('aswinger', words=_WORDS))
        expected = 'swearing'
        self.assertIn(expected, actual)

    def test_rejoiced(self):
        '''featured in 8 out 10 cats does Countdown'''
        actual = list(wordgame.countdown('joecried', words=_WORDS))
        expected = 'rejoiced'
        self.assertIn(expected, actual)


class TestCanWordBeMadeWithLetters(unittest.TestCase):
    def test_positive(self):
        actual = wordgame._can_word_be_made_with_letters(
            word='bad',
            letters='abcd')
        self.assertTrue(actual)

    def test_negative(self):
        actual = wordgame._can_word_be_made_with_letters(
            word='other',
            letters='abcd')
        self.assertFalse(actual)

    def test_swearing(self):
        '''featured in 8 out 10 cats does Countdown'''
        actual = wordgame._can_word_be_made_with_letters(
            word='swearing',
            letters='aswinger')
        self.assertTrue(actual)

    def test_rejoiced(self):
        '''featured in 8 out 10 cats does Countdown'''
        actual = wordgame._can_word_be_made_with_letters(
            word='rejoiced',
            letters='joecried')
        self.assertTrue(actual)


@patch("builtins.open")
class TestFindListOfWords(unittest.TestCase):
    def test_trailing_new_lines_are_removed(self, mock_open):
        given = ['abc\n', 'def\n']
        mock_open.return_value.__enter__ = mock_open
        mock_open.return_value.__iter__.return_value = iter(given)
        actual = list(wordgame._find_list_of_words())
        expected = ['abc', 'def']
        self.assertEqual(actual, expected)
