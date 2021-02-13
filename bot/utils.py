import re

from discord import Message


def is_message_overwatch_time(message: Message) -> bool:
    """
    Returns True/False if the message's content looks like it's for Overwatch
    :param message: The Message from Discord
    :return: bool: True/False if it's time for Overwatch
    """
    message.content = message.content.lower()
    qualifiers = list()
    # Ends with multiple a's
    qualifiers.append(re.search(r'(aa+)\b', message.content) is not None)
    qualifiers.append(message.content == 'a')
    qualifiers.append(message.content == 'i a soon')
    qualifiers.append(is_long_form_overwatch_time(message))
    return any(qualifiers)


# Maybe one day this will be done with ML but Today that day isn't
def is_long_form_overwatch_time(message: Message) -> bool:
    """
    Returns True/False if the message's content looks like it's for Overwatch but more complex
    Tries to match messages like:
    I a in 20 minutes
    I can a for 45 mins
    I can a in 7
    :param message: The Message from Discord
    :return: bool: True/False if message's content looks like it's for Overwatch
    """
    contains_verbs = any(verb in message.content for verb in ['can', 'will', 'able to'])
    contains_a = ' a ' in message.content
    contains_i = message.content[0] == 'i'
    contains_adverbs = any(adverb in message.content for adverb in ['little', 'soon', 'shortly'])
    contains_qualifiers = any(qualifier in message.content for qualifier in ['in', 'for'])
    contains_time = re.search(r'\d+', message.content) is not None
    # Must have I <verb> a
    # Can either say a time via adverb or a digit time with a qualifier
    return contains_a and contains_i and contains_verbs and (contains_adverbs or contains_qualifiers and contains_time)
