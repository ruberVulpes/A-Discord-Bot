import re

import discord

from bot import logger

client = discord.Client()

a_pattern = r'(aa+)\b'


@client.event
async def on_ready():
    logger.info(f'{client.user} has connected to Discord!')
    logger.info(f'Connected to Guilds {[guild.name for guild in client.guilds]}')


@client.event
async def on_message(message: discord.Message):
    # Ignore any messages from myself just in case
    if message.author == client.user:
        return

    if re.search(a_pattern, message.content) or message.content == 'a':
        logger.debug(f'Reacting to message: {message.content}')
        await message.add_reaction(emoji='🅰️')
        await message.add_reaction(emoji='❗')
