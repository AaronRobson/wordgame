import argparse

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
    return parser


def _main():
    parser = _make_parser()
    settings = parser.parse_args()
    if settings.game != 'countdown':
        raise NotImplementedError('Only the countdown game type is currently supported.')
    results = wordgame.countdown(settings.letters)
    for result in results:
        print(result)


if __name__ == '__main__':
    _main()
