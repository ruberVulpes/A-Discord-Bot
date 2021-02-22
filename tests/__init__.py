from dataclasses import dataclass, field
from typing import List


@dataclass
class IDName:
    id: str = '1234'
    name: str = 'my-name'


class Channel(IDName):
    async def send(self, *args, **kwargs):
        pass


@dataclass
class TestMessage:
    content: str = 'content'
    guild: IDName = IDName(name='my-guild')
    channel: IDName = Channel(name='my-channel')
    author: IDName = IDName(name='some-user')

    async def add_reaction(self,*args, **kwargs):
        pass


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
