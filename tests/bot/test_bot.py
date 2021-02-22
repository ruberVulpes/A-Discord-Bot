from typing import Callable
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from bot.bot import on_message, on_ready
from db import session
from db.models import MessageHistory
from tests import TestMessage


class Test(IsolatedAsyncioTestCase):
    def setUp(self):
        session.query(MessageHistory).delete()

    # noinspection PyUnusedLocal
    @patch('bot.bot.get_reaction_gif', side_effect=lambda: '')
    async def test_on_message(self, mock_get_reaction_gif: Callable):
        await on_message(TestMessage(content=''))
        await on_message(TestMessage(content='a'))
        await on_message(TestMessage(author=None))
        await on_message(TestMessage(content='a time leggo'))

    async def test_on_ready(self):
        await on_ready()

    def tearDown(self):
        session.query(MessageHistory).delete()
