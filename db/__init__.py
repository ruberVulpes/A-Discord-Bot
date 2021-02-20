from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from env import database_url

engine = create_engine(database_url)
session = sessionmaker(bind=engine)()
