from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

from db import engine

Base = declarative_base()


class MessageHistory(Base):
    __tablename__ = "message-history"
    id = Column(Integer, primary_key=True)
    guild_id = Column(Integer)
    channel_id = Column(Integer)
    last_posted = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.__class__.__name__}(Guild={self.guild_id}, Channel={self.channel_id}, {self.last_posted})'


# Create Tables
Base.metadata.create_all(engine)
