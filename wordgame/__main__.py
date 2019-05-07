import argparse
from itertools import islice

import wordgame

_GAME_CHOICES = [
    'countdown',
]

_DEFAULT_GAME_CHOICE = _GAME_CHOICES[0]


def _make_parser():
    parser = argparse.ArgumentParser(
        prog='wordgame',
        description='Solve for wordgames such as scrabble and countdown.',
    )
    parser.add_argument(
        'letters',
        metavar='LETTERS',
        help='the letters to use',
    )
    parser.add_argument(
        '-g', '--game',
        metavar='GAME',
        choices=_GAME_CHOICES,
        default=_DEFAULT_GAME_CHOICE,
        help='which wordgame to play',
    )
    parser.add_argument(
        '-n', '--maximum-number-of-results',
        type=int,
        help='maximum number of results to return (default: all results)',
    )
    return parser


def take(n, sequence):
    try:
        return islice(sequence, n)
    except ValueError:
        return []


def _main():
    parser = _make_parser()
    settings = parser.parse_args()
    if settings.game != 'countdown':
        raise NotImplementedError(
            'Only the countdown game type is currently supported.')
    results = wordgame.countdown(settings.letters)

    results = take(
        settings.maximum_number_of_results,
        results)

    for result in results:
        print(result)


if __name__ == '__main__':
    _main()
