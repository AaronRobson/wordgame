from collections import Counter
from os import path

from string import ascii_letters

_COUNTDOWN_LETTER_COUNT = 9
_COUNTDOWN_LETTER_COUNT_FOR_TEASER = 8


def countdown(letters, words=None, sort=True, skip_letters_validation=False):
    if not skip_letters_validation:
        letters = validate_countdown_letters(letters)
    else:
        letters = letters.lower()

    if words is None:
        words = _find_list_of_words()
    words = (word.lower() for word in words)

    allowed_words_by_length = filter(
        length_predicate(max_length=len(letters)),
        words
    )
    results = (
        word
        for word in allowed_words_by_length
        if _can_word_be_made_with_letters(word=word, letters=letters))

    if sort:
        results = sort_words(results)

    return results


# From: http://www.thecountdownpage.com/letters.htm
_LETTER_DISTRIBUTION = {
    'a': 15,
    'e': 21,
    'i': 13,
    'o': 13,
    'u': 5,

    'b': 2,
    'c': 3,
    'd': 6,
    'f': 2,
    'g': 3,
    'h': 2,
    'j': 1,
    'k': 1,
    'l': 5,
    'm': 4,
    'n': 8,
    'p': 4,
    'q': 1,
    'r': 9,
    's': 9,
    't': 9,
    'v': 1,
    'w': 1,
    'x': 1,
    'y': 1,
    'z': 1,
}


def validate_countdown_letters(letters):
    if len(letters) not in [
            _COUNTDOWN_LETTER_COUNT,
            _COUNTDOWN_LETTER_COUNT_FOR_TEASER]:
        raise ValueError(
            f'There must be {_COUNTDOWN_LETTER_COUNT} letters '
            f'or {_COUNTDOWN_LETTER_COUNT_FOR_TEASER} for teasers '
            'to play countdown.')
    for letter in letters:
        if letter not in ascii_letters:
            raise ValueError(
                f'{repr(letter)} is not a valid letter in countdown')
    letters = letters.lower()
    for letter in sorted(list(set(letters))):
        count_of_a_letter = letters.count(letter)
        max_allowed = _LETTER_DISTRIBUTION[letter]
        if max_allowed < count_of_a_letter:
            raise ValueError(
                f'There are too many {letter}s found in the countdown letters '
                f'{count_of_a_letter} found '
                f'but only {max_allowed} are allowed')
    return letters


class PartiallyOrderedCounter(Counter):
    '''Source: https://stackoverflow.com/a/44644868/1011785'''

    def __le__(self, other):
        """ Multiset inclusion """
        return all(v <= other[k] for k, v in self.items())

    def __lt__(self, other):
        """ Multiset strict inclusion """
        return self <= other and self != other

    # TODO : __ge__ and __gt__
    # Beware : they CANNOT be written in terms of __le__ or __lt__


def _can_word_be_made_with_letters(letters, word):
    return PartiallyOrderedCounter(word) <= PartiallyOrderedCounter(letters)


def _find_list_of_words():
    word_list_filepath = path.join(
        path.dirname(__file__),
        '..',
        'words.txt')
    with open(word_list_filepath, 'r') as f:
        for line in f:
            yield line.strip()


def length_predicate(max_length):
    def pred(value):
        return len(value) <= max_length
    return pred


def sort_words(words):
    return sorted(
        sorted(words),
        key=len,
        reverse=True)
