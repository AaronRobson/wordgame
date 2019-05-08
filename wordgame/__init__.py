from collections import Counter

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
    with open('words.txt', 'r') as f:
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
