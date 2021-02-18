from dataclasses import dataclass
from unittest import TestCase

from bot import utils


@dataclass
class IDName:
    id: str = '1234'
    name: str = 'my-name'


@dataclass
class TestMessage:
    content: str = 'content'
    guild: IDName = IDName(name='my-guild')
    channel: IDName = IDName(name='my-channel')


class Test(TestCase):
    def test_is_message_overwatch_time_basic(self):
        success_test_cases = ['a', 'aaa', "let's aaaaa", 'i a soon']
        failure_test_cases = ['i really want to go to the store', "rimworld", "gorilla", "king kong", "i can't a",
                              'busy', "can't tonight"]
        for success_test_case in success_test_cases:
            self.assertTrue(utils.is_message_overwatch_time_basic(success_test_case))

        for failure_test_case in failure_test_cases:
            self.assertFalse(utils.is_message_overwatch_time_basic(failure_test_case))

    def test_is_message_overwatch_time_linear_regression(self):
        success_test_cases = ['i a in 20 minutes', 'i can a for 45 mins', 'i can a in 7']
        failure_test_cases = ['i really want to go to the store', "rimworld", "gorilla", "king kong", "i can not a",
                              'busy', "can not tonight"]
        for success_test_case in success_test_cases:
            self.assertTrue(utils.is_message_overwatch_time_linear_regression(success_test_case))

        for failure_test_case in failure_test_cases:
            self.assertFalse(utils.is_message_overwatch_time_linear_regression(failure_test_case))

    def test_get_clean_message_content(self):
        test_strings = {'```a```': '', 'a': 'a', '`a`': '', "```python print('Hello World!')```": '',
                        'https://google.com': '', 'https://gph.is/st/Y6a9pWQ': ''}
        test_message_object = TestMessage()
        for function_input, expected_output in test_strings.items():
            test_message_object.content = function_input
            self.assertEqual(utils.get_clean_message_content(test_message_object), expected_output)

    def test_is_spam(self):

        def _test_is_spam(test_message: TestMessage):
            self.assertFalse(utils.is_spam(test_message))
            self.assertTrue(utils.is_spam(test_message))

        _test_is_spam(TestMessage())
        # Test New Guild
        _test_is_spam(TestMessage(guild=IDName('my-new-guild-id')))
        # Test Old Guild, but different channel
        _test_is_spam(TestMessage(channel=IDName('my-new-channel-id')))
