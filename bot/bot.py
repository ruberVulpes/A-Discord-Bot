import discord

from bot import logger, utils
from bot.giphy import get_reaction_gif

client = discord.Client()


@client.event
async def on_ready():
    logger.info(f'{client.user} has connected to Discord!')
    logger.info(f'Connected to Guilds {[guild.name for guild in client.guilds]}')


@client.event
async def on_message(message: discord.Message):
    # Ignore any messages from myself just in case
    if message.author == client.user:
        return
    if utils.is_message_overwatch_time(utils.get_clean_message_content(message)):
        logger.debug(f'Reacting to message: {message.content}')
        await message.add_reaction(emoji='🅰️')
        await message.add_reaction(emoji='❗')
        await message.channel.send(get_reaction_gif())
