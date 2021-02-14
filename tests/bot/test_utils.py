from collections import namedtuple
from unittest import TestCase

from bot import utils

TestMessageObject = namedtuple('TestMessageObject', 'content')


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
        for function_input, expected_output in test_strings.items():
            self.assertEqual(utils.get_clean_message_content(TestMessageObject(function_input)), expected_output)
