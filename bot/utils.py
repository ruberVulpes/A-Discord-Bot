import re

from discord import Message
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

import ml
from bot import logger
from ml import cutoff


def is_message_overwatch_time_basic(cleaned_message_content: str) -> bool:
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
    qualifiers.append(cleaned_message_content == 'overwatch')
    qualifiers.append(cleaned_message_content == 'o v e r w a t c h')
    return any(qualifiers)


def is_message_overwatch_time_linear_regression(cleaned_message_content: str) -> bool:
    """
    Returns True/False if the message's content looks like it's for Overwatch using a linear regression model
    :param cleaned_message_content: The messages cleaned content (can be gotten from utils.get_clean_message_content)
    :return: bool: True/False if message's content looks like it's for Overwatch
    """
    classifier: LogisticRegression = load(ml.model_path)
    vectorizer: CountVectorizer = load(ml.vectorizer_path)
    decision_result = classifier.decision_function(vectorizer.transform([cleaned_message_content[:cutoff]]))[0]
    logger.info(f'msg:{cleaned_message_content[:cutoff]}, result:{decision_result}')
    # > 0 is considered a match, but let's try not to spam
    return decision_result > .25


def get_clean_message_content(message: Message) -> str:
    """
    Returns a cleaned content string for the message
    The cleaned content string is lower case without code blocks or inline code
    :param message: The Message object from Discord
    :return: str: The cleaned content string
    """
    # Code Blocks, Inline Code, URLS
    regex_patterns = [r'```[\s\S]*```', r'`[\s\S]*`', r'^https?:\/\/.*[\r\n]*']
    # To Lower Case
    content: str = message.content.lower()
    content = content.replace("can't", 'can not')

    # Apply Regex Cleaning
    for regex_pattern in regex_patterns:
        for match in re.findall(regex_pattern, content):
            content = content.replace(match, '')

    return content
