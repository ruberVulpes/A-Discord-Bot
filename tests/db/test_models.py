from unittest import TestCase

from db.models import MessageHistory


class TestMessageHistory(TestCase):
    def test_repr(self):
        MessageHistory(guild_id=1234, channel_id=1234).__repr__()
