import unittest

from wordgame import _find_list_of_words


def _contains_whitespace(text):
    if not text:
        return False

    parts = text.split()
    return not (len(parts) == 1 and text == parts[0])


class TestWordsList(unittest.TestCase):
    '''Tests that the contents of the words.txt file are valid'''
    @classmethod
    def setUpClass(cls):
        cls.words = list(_find_list_of_words())

    def test_no_empty_string_words(self):
        for word in self.words:
            self.assertNotEqual(len(word), 0)

    def test_no_whitespace_is_present(self):
        self.assertFalse(any(map(_contains_whitespace, self.words)))

    def test_all_words_are_alphabetical(self):
        for word in self.words:
            self.assertTrue(word.isalpha())
