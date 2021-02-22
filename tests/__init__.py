from dataclasses import dataclass, field
from typing import List


@dataclass
class IDName:
    id: str = '1234'
    name: str = 'my-name'


@dataclass
class TestMessage:
    content: str = 'content'
    guild: IDName = IDName(name='my-guild')
    channel: IDName = IDName(name='my-channel')


@dataclass
class TestGiphySearchElement:
    bitly_url: str = 'http://gph.is/2lF27bG'


@dataclass
class TestGiphySearch:
    api_key: str
    q: str
    lang: str
    rating: str
    data: List[TestGiphySearchElement] = field(default_factory=lambda: [TestGiphySearchElement()])
