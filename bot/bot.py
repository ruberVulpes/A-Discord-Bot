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

    clean_message_content = utils.get_clean_message_content(message)
    # Skip any empty messages once cleaned
    if len(clean_message_content) == 0:
        return

    basic_match = utils.is_message_overwatch_time_basic(clean_message_content)
    ml_match = utils.is_message_overwatch_time_linear_regression(clean_message_content)

    if basic_match or ml_match:
        logger.debug(f'Reacting to message: {message.content}')
        await message.add_reaction(emoji='🅰️')
        await message.add_reaction(emoji='❗')
        if ml_match and not basic_match:
            await message.add_reaction(emoji='🤖')
        # Utilize message cool down
        if utils.is_spam(message):
            await message.add_reaction(emoji='⏳')
        else:
            await message.channel.send(get_reaction_gif())
