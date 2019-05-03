from collections import Counter


def countdown(letters, max_length=9, words=None):
    if words is None:
        words = _find_list_of_words()

    allowed_words_by_length = filter(
        length_predicate(max_length),
        words
    )
    for word in allowed_words_by_length:
        if _can_word_be_made_with_letters(word=word, letters=letters):
            yield word


def _can_word_be_made_with_letters(letters, word):
    values = Counter(letters) - Counter(word)
    return values == +values


def _find_list_of_words():
    with open('words.txt', 'r') as f:
        return f.readlines()


def length_predicate(max_length):
    def pred(value):
        return len(value) <= max_length
    return pred
