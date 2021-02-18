from dataclasses import dataclass


@dataclass
class IDName:
    id: str = '1234'
    name: str = 'my-name'


@dataclass
class TestMessage:
    content: str = 'content'
    guild: IDName = IDName(name='my-guild')
    channel: IDName = IDName(name='my-channel')
