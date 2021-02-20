import os

discord_token = os.environ['DISCORD_TOKEN']

giphy_token = os.environ['GIPHY_TOKEN']

# Use sqlite memory db for tests
database_url = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
