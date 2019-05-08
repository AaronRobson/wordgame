import unittest

from wordgame import _find_list_of_words


class TestWordsList(unittest.TestCase):
    '''Tests that the contents of the words.txt file are valid'''
    @classmethod
    def setUpClass(cls):
        cls.words = list(_find_list_of_words())

    def test_no_empty_string_words(self):
        for word in self.words:
            self.assertNotEqual(len(word), 0)

    def test_no_whitespace_are_present(self):
        for word in self.words:
            for character in word:
                self.assertFalse(character.isspace())

    def test_all_words_are_alphabetical(self):
        for word in self.words:
            self.assertTrue(word.isalpha())
