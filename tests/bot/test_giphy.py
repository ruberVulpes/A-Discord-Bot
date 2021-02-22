from typing import Callable
from unittest import TestCase
from unittest.mock import patch

from bot.giphy import get_reaction_gif
from tests import TestGiphySearch


class Test(TestCase):
    # noinspection PyUnusedLocal
    # skipcq: PYL-W0613
    @patch('bot.giphy.giphy.gifs_search_get', side_effect=TestGiphySearch)
    def test_get_reaction_gif(self, mock_gifs_search_get: Callable):
        self.assertTrue(isinstance(get_reaction_gif(), str))
