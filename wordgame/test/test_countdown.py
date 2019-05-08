import unittest
from unittest.mock import patch

import wordgame

_WORDS = [
    'bad',
    'rejoiced',
    'swearing',
]


class TestCountdown(unittest.TestCase):
    def setUp(self):
        self._WORDS_UPPER = [word.upper() for word in _WORDS]

    def test_simple(self):
        actual = list(wordgame.countdown(
            'abcd',
            words=_WORDS,
            skip_letters_validation=True))
        expected = 'bad'
        self.assertIn(expected, actual)

    def test_upper_case_letters(self):
        actual = list(wordgame.countdown(
            'ABCD',
            words=_WORDS,
            skip_letters_validation=True))
        expected = 'bad'
        self.assertIn(expected, actual)

    def test_upper_case_words(self):
        actual = list(wordgame.countdown(
            'abcd',
            words=self._WORDS_UPPER,
            skip_letters_validation=True))
        expected = 'bad'
        self.assertIn(expected, actual)

    def test_upper_case_letters_and_words(self):
        actual = list(wordgame.countdown(
            'ABCD',
            words=self._WORDS_UPPER,
            skip_letters_validation=True))
        expected = 'bad'
        self.assertIn(expected, actual)

    def test_swearing(self):
        '''featured in 8 out 10 cats does Countdown'''
        actual = list(wordgame.countdown(
            'aswinger',
            words=_WORDS,
            skip_letters_validation=True))
        expected = 'swearing'
        self.assertIn(expected, actual)

    def test_rejoiced(self):
        '''featured in 8 out 10 cats does Countdown'''
        actual = list(wordgame.countdown(
            'joecried',
            words=_WORDS,
            skip_letters_validation=True))
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


class TestValidateCountdownLetters(unittest.TestCase):
    def test_valid_letters(self):
        expected = given = 'fdofieasg'
        actual = wordgame.validate_countdown_letters(
            letters=given)
        self.assertEqual(actual, expected)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            wordgame.validate_countdown_letters(
                letters='abc'
            )

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            wordgame.validate_countdown_letters(
                letters='abcdefgh#'
            )

    def test_invalid_amount_of_a_letter(self):
        with self.assertRaises(ValueError):
            wordgame.validate_countdown_letters(
                letters='xxabcdefg'
            )


@patch("builtins.open")
class TestFindListOfWords(unittest.TestCase):
    def test_trailing_new_lines_are_removed(self, mock_open):
        given = ['abc\n', 'def\n']
        mock_open.return_value.__enter__ = mock_open
        mock_open.return_value.__iter__.return_value = iter(given)
        actual = list(wordgame._find_list_of_words())
        expected = ['abc', 'def']
        self.assertEqual(actual, expected)
