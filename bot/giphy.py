import random
from typing import Optional, List

import giphy_client

from env import giphy_token

giphy = giphy_client.DefaultApi()


def get_reaction_gif(query_strings: Optional[List[str]] = None) -> str:
    """
    Queries Giphy for a gif from either the default query strings or ones passed in
    :param query_strings: An optional list of query strings to use to find gifs
    :return: str: A short giphy url to the gif
    """
    query_strings = query_strings or ['overwatch', 'gorillas', 'dance']
    query_string = random.choice(query_strings)
    search_result = giphy.gifs_search_get(api_key=giphy_token, q=query_string, lang='en', rating='pg-13')
    return random.choice(search_result.data).bitly_url
