import asyncio
import sys

import discord
import signal

from utilities import config
from discord.ext import commands
from src.cogs.HELP import HELP

intents = discord.Intents.all()  # Should probably fix this at some point

bot = commands.Bot(command_prefix='&', intents=intents, help_command=None)
extensions = ('src.cogs.events.events', 'src.cogs.aesthetic.aesthetic', 'src.cogs.creatures.creatures',
              'src.cogs.f_respects.f', 'src.cogs.palette.palette', 'src.cogs.person.person', 'src.cogs.prompts.prompts',
              'src.cogs.plant_gen.plant', 'src.cogs.emoji_gen.emoji_generator',
              'src.cogs.color_generator.color_generator', 'src.cogs.HELP')


async def handler():
    await bot.close()
    sys.exit()


async def load_extensions():
    print('Loading commands...')
    for ext in extensions:
        await bot.load_extension(ext)


async def main():
    async with bot:
        await load_extensions()
        TOKEN = config.DISCORD_SECRET_TOKEN

        for signal_name in ('SIGINT', 'SIGTERM'):
            bot.loop.add_signal_handler(getattr(signal, signal_name), lambda: asyncio.ensure_future(handler()))

        await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())

'''
@bot.command()
async def embedded(ctx):  # This is just for testing purposes of embedding. Ignore.
    embed = discord.Embed(
        title='Test Title',
        description='Test Description',
        colour=discord.Colour(color)
    )

    file = discord.File('galaxy.jpg', filename='image.jpg')

    embed.set_footer(text='This is a footer')
    embed.set_image(url='attachment://image.jpg')
    embed.set_footer(text='This is a footer')
    embed.set_thumbnail(url='attachment://image.jpg')
    embed.set_author(name='Meee! :D', icon_url='attachment://image.jpg')
    embed.add_field(name='Field Name', value='Field Value1', inline=True)
    embed.add_field(name='Field Name', value='Field Value2', inline=True)
    embed.add_field(name='Field Name', value='Field Value3', inline=False)

    await ctx.channel.send(file=file, embed=embed)
'''
