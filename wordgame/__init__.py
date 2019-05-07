from collections import Counter


def countdown(letters, max_length=9, words=None, sort=True):
    if words is None:
        words = _find_list_of_words()

    allowed_words_by_length = filter(
        length_predicate(max_length),
        words
    )
    results = (
        word
        for word in allowed_words_by_length
        if _can_word_be_made_with_letters(word=word, letters=letters))

    if sort:
        results = sort_words(results)

    return results


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
