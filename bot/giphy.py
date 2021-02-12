import random
from typing import Optional, List

import giphy_client

from env import giphy_token

giphy = giphy_client.DefaultApi()


def get_reaction_gif(query_strings: Optional[List[str]] = None) -> str:
    query_strings = query_strings or ['overwatch', 'gorillas', 'dance']
    query_string = random.choice(query_strings)
    return random.choice(giphy.gifs_search_get(api_key=giphy_token, q=query_string, lang='en').data).bitly_url
