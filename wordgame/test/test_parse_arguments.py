import unittest

from wordgame.__main__ import _make_parser


class TestMakeParser(unittest.TestCase):
    def setUp(self):
        self.parser = _make_parser()

    def test_game_argument_default(self):
        settings = self.parser.parse_args(['abc'])
        self.assertEqual(settings.game, 'countdown')
