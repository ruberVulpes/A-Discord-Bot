import re

from discord import Message


def is_message_overwatch_time(cleaned_message_content: str) -> bool:
    """
    Returns True/False if the message's content looks like it's for Overwatch
    :param cleaned_message_content: The messages cleaned content (can be gotten from utils.get_clean_message_content)
    :return: bool: True/False if it's time for Overwatch
    """
    qualifiers = list()
    # Ends with multiple a's
    qualifiers.append(re.search(r'(aa+)\b', cleaned_message_content) is not None)
    qualifiers.append(cleaned_message_content == 'a')
    qualifiers.append(cleaned_message_content == 'i a soon')
    qualifiers.append(_is_long_form_overwatch_time(cleaned_message_content))
    return any(qualifiers)


# Maybe one day this will be done with ML but Today that day isn't
def _is_long_form_overwatch_time(cleaned_message_content: str) -> bool:
    """
    Returns True/False if the message's content looks like it's for Overwatch but more complex
    Tries to match messages like:
    I a in 20 minutes
    I can a for 45 mins
    I can a in 7
    :param cleaned_message_content: The messages cleaned content (can be gotten from utils.get_clean_message_content)
    :return: bool: True/False if message's content looks like it's for Overwatch
    """
    contains_a = ' a ' in cleaned_message_content
    # Index safe way of checking to see if message starts with I
    contains_i = cleaned_message_content.find('i') == 0
    contains_adverbs = any(adverb in cleaned_message_content for adverb in ['little', 'soon', 'shortly'])
    contains_qualifiers = any(qualifier in cleaned_message_content for qualifier in ['in', 'for'])
    contains_time = re.search(r'\d+', cleaned_message_content) is not None
    # Must have I <verb> a
    # Can either say a time via adverb or a digit time with a qualifier
    return contains_a and contains_i and (contains_adverbs or contains_qualifiers and contains_time)


def get_clean_message_content(message: Message) -> str:
    """
    Returns a cleaned content string for the message
    The cleaned content string is lower case without code blocks or inline code
    :param message: The Message object from Discord
    :return: str: The cleaned content string
    """
    # Code Blocks, Inline Code
    regex_patterns = [r'```[\s\S]*```', r'`[\s\S]*`']
    # To Lower Case
    content: str = message.content.lower()

    # Apply Regex Cleaning
    for regex_pattern in regex_patterns:
        for match in re.findall(regex_pattern, content):
            content = content.replace(match, '')

    return content
