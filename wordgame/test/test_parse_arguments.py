import unittest

from wordgame.__main__ import _make_parser


class TestMakeParser(unittest.TestCase):
    def setUp(self):
        self.parser = _make_parser()

    def test_game_argument_default(self):
        settings = self.parser.parse_args(['abc'])
        self.assertEqual(settings.game, 'countdown')
        self.assertIsNone(settings.maximum_number_of_results)

    def test_number(self):
        settings = self.parser.parse_args(['abc', '-n', '5'])
        self.assertEqual(settings.maximum_number_of_results, 5)
